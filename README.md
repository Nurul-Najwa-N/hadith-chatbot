# ☪️ Hadith Information Retrieval System
### Entity-Aware RAG Pipeline · NLP · Named Entity Recognition · Fuzzy Matching

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url.streamlit.app)
[![IEEE Paper](https://img.shields.io/badge/IEEE-Published-blue)](https://ieeexplore.ieee.org/document/11488814)

A production-ready AI chatbot for retrieving and understanding Islamic Hadith, built with an Entity-Aware RAG (Retrieval-Augmented Generation) pipeline.

---

## 🏗️ Architecture

```
User Query
    │
    ▼
Named Entity Recognition (NER)
    │  Detects: Prophets, Companions, Islamic concepts
    ▼
Fuzzy Query Expansion
    │  Handles Arabic name variations (e.g. "Muhammed" → "Muhammad")
    │  Improved retrieval from 6/14 → 13/14 topics (FYP evaluation)
    ▼
Vector Search (ChromaDB)
    │  Semantic similarity across 25+ authentic Hadiths
    ▼
LLM Synthesis (Claude)
    │  Generates grounded, cited answer
    ▼
Response with sources + relevance scores
```

## ✨ Features

- **Entity-Aware Retrieval** — NER detects Islamic entities to improve search precision
- **Fuzzy Matching** — handles Arabic transliteration variations
- **Semantic Search** — ChromaDB vector store for similarity-based retrieval
- **Source Citations** — every answer cites specific Hadith collection and reference
- **Relevance Scoring** — shows retrieval confidence per Hadith
- **Adjustable Settings** — control top-k results, toggle NER and fuzzy matching

## 📊 Evaluation Results

| Metric | Before Fuzzy Matching | After Fuzzy Matching |
|--------|----------------------|---------------------|
| Theme Coverage | 6/14 topics | 13/14 topics |
| Precision@5 | 0.62 | 0.81 |
| MRR@5 | 0.58 | 0.79 |

## 🗂️ Hadith Collections

| Collection | Description |
|-----------|-------------|
| Sahih Bukhari | Most authentic collection |
| Sahih Muslim | Second most authentic |
| Sunan Abu Dawud | Major Sunan collection |
| Sunan Tirmidhi | Major Sunan collection |
| Sunan Ibn Majah | Major Sunan collection |

## 🚀 Run Locally

```bash
# Clone repo
git clone https://github.com/Nurul-Najwa-N/hadith-rag-chatbot.git
cd hadith-rag-chatbot

# Install dependencies
pip install -r requirements.txt

# Add your API key
echo 'ANTHROPIC_API_KEY = "your-key-here"' > .streamlit/secrets.toml

# Run
streamlit run app.py
```

## 🔬 Research Background

This project is a portfolio implementation based on my IEEE-published Final Year Project:

**"The Development of Information Retrieval Model for Hadith Data from Knowledge Graph"**
*Nurul Najwa Norhisham, Noryanti Muhammad, Mohd Izhar Firdaus Ismail, Aleta Caras Fabregas*
📄 [Read on IEEE Xplore](https://ieeexplore.ieee.org/document/11488814)

**Differences from FYP:**
| | FYP (Original) | This Portfolio Version |
|--|--|--|
| Vector Store | Neo4j Knowledge Graph | ChromaDB |
| LLM | Ollama LLaMA 3.2 (local) | Claude API |
| Deployment | Local only | Streamlit Cloud (public) |
| Purpose | Academic research | Portfolio demonstration |

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Vector DB**: ChromaDB
- **LLM**: Anthropic Claude (claude-sonnet-4-20250514)
- **NLP**: Custom NER + fuzzy matching (difflib)
- **Deployment**: Streamlit Community Cloud (free)

## 👩‍💻 Author

**Nurul Najwa Norhisham**
- 🔗 [LinkedIn](https://linkedin.com/in/nurul-najwa-norhisham)
- 🐙 [GitHub](https://github.com/Nurul-Najwa-N)
- 📧 nurulnajwanorhisham02@gmail.com
- 📄 [IEEE Publication](https://ieeexplore.ieee.org/document/11488814)
