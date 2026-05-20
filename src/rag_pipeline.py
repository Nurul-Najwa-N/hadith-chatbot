import re
import json
from google import genai
import chromadb
from chromadb.utils import embedding_functions
from difflib import SequenceMatcher
from src.hadith_data import HADITH_DATASET, ISLAMIC_ENTITIES

class HadithRAG:
    """
    Entity-Aware RAG Pipeline for Hadith Information Retrieval.

    Architecture (simplified from IEEE-published FYP):
    - NER: Named Entity Recognition for Islamic terms
    - Fuzzy Matching: handles Arabic name transliteration variations
    - Vector Search: ChromaDB for semantic similarity
    - LLM: Gemini for answer synthesis

    Original FYP used Neo4j knowledge graph + Ollama LLaMA 3.2.
    This portfolio version uses ChromaDB + Gemini API for free deployment.
    """

    def __init__(self, api_key: str):
        self.client = genai.Client(api_key=api_key)
        self._init_vectorstore()

    def _init_vectorstore(self):
        """Initialise ChromaDB with Hadith dataset."""
        self.chroma = chromadb.Client()
        ef = embedding_functions.DefaultEmbeddingFunction()

        try:
            self.collection = self.chroma.get_collection("hadiths")
        except Exception:
            self.collection = self.chroma.create_collection(
                name="hadiths",
                embedding_function=ef,
                metadata={"hnsw:space": "cosine"}
            )
            # Load dataset
            docs, ids, metas = [], [], []
            for i, h in enumerate(HADITH_DATASET):
                docs.append(h["text"])
                ids.append(f"hadith_{i}")
                metas.append({
                    "collection": h["collection"],
                    "reference": h["reference"],
                    "arabic": h.get("arabic", ""),
                    "topics": json.dumps(h.get("topics", [])),
                    "narrator": h.get("narrator", "")
                })
            self.collection.add(documents=docs, ids=ids, metadatas=metas)

    # ── NER ───────────────────────────────────────────────────────────────────
    def extract_entities(self, query: str) -> list[str]:
        """
        Named Entity Recognition for Islamic terms.
        Detects: Prophets, Companions, Islamic concepts, Arabic terms.
        """
        found = []
        query_lower = query.lower()
        for entity, aliases in ISLAMIC_ENTITIES.items():
            for alias in aliases:
                if alias.lower() in query_lower:
                    found.append(entity)
                    break
        return list(set(found))

    # ── FUZZY MATCHING ────────────────────────────────────────────────────────
    def fuzzy_expand_query(self, query: str, threshold: float = 0.75) -> str:
        """
        Fuzzy matching for Arabic name variations.
        e.g. 'Muhammed' → 'Muhammad', 'Aisha' → 'Aisha/Aishah'
        Improved retrieval from 6/14 to 13/14 topics in FYP evaluation.
        """
        words = query.split()
        expanded = []
        all_aliases = []
        for aliases in ISLAMIC_ENTITIES.values():
            all_aliases.extend(aliases)

        for word in words:
            best_match = word
            best_score = 0
            for alias in all_aliases:
                score = SequenceMatcher(None, word.lower(), alias.lower()).ratio()
                if score > best_score and score >= threshold:
                    best_score = score
                    best_match = alias
            expanded.append(best_match)
        return " ".join(expanded)

    # ── VECTOR SEARCH ─────────────────────────────────────────────────────────
    def retrieve(self, query: str, top_k: int = 5) -> list[dict]:
        """Semantic similarity search using ChromaDB."""
        results = self.collection.query(
            query_texts=[query],
            n_results=min(top_k, len(HADITH_DATASET))
        )
        hadiths = []
        for i, doc in enumerate(results["documents"][0]):
            meta = results["metadatas"][0][i]
            distance = results["distances"][0][i]
            score = round(1 - distance, 3)
            hadiths.append({
                "text": doc,
                "collection": meta["collection"],
                "reference": meta["reference"],
                "arabic": meta.get("arabic", ""),
                "narrator": meta.get("narrator", ""),
                "topics": json.loads(meta.get("topics", "[]")),
                "score": score
            })
        return hadiths

    # ── LLM SYNTHESIS ─────────────────────────────────────────────────────────
    def synthesise(self, query: str, hadiths: list[dict], entities: list[str]) -> str:
        """Use Gemini to synthesise a final answer from retrieved Hadiths."""
        context = "\n\n".join([
            f"[{h['collection']} - {h['reference']}]\n{h['text']}"
            for h in hadiths
        ])
        entity_str = f"Detected entities: {', '.join(entities)}" if entities else ""

        prompt = f"""You are a knowledgeable Islamic scholar assistant.
Answer the user's question based ONLY on the provided Hadith texts.
Be respectful, accurate, and cite the specific collections.
If the Hadiths don't directly answer the question, say so honestly.

{entity_str}

Retrieved Hadiths:
{context}

User Question: {query}

Provide a clear, helpful answer that:
1. Directly addresses the question
2. References specific Hadiths by collection name
3. Is respectful and educational in tone
4. Mentions if there are multiple relevant narrations"""

        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return response.text

    # ── MAIN QUERY ────────────────────────────────────────────────────────────
    def query(self, query: str, top_k: int = 5,
              use_fuzzy: bool = True, use_ner: bool = True) -> dict:
        """
        Full RAG pipeline:
        Query → NER → Fuzzy Expand → Retrieve → Synthesise
        """
        entities = self.extract_entities(query) if use_ner else []
        expanded_query = self.fuzzy_expand_query(query) if use_fuzzy else query
        # Enrich query with detected entities
        if entities:
            expanded_query = f"{expanded_query} {' '.join(entities)}"
        hadiths = self.retrieve(expanded_query, top_k=top_k)
        answer = self.synthesise(query, hadiths, entities)
        return {
            "query": query,
            "expanded_query": expanded_query,
            "entities": entities,
            "hadiths": hadiths,
            "answer": answer
        }

    def get_stats(self) -> dict:
        return {
            "total_hadiths": len(HADITH_DATASET),
            "collections": len(set(h["collection"] for h in HADITH_DATASET))
        }
