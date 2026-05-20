import streamlit as st
import os
from src.rag_pipeline import HadithRAG

# ── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Hadith RAG Chatbot",
    page_icon="☪️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 1rem 0;
        border-bottom: 2px solid #1f4e79;
        margin-bottom: 1.5rem;
    }
    .main-header h1 { color: #1f4e79; font-size: 2rem; }
    .main-header p { color: #555; font-size: 0.9rem; }

    .hadith-card {
        background: #f8f9fa;
        border-left: 4px solid #1f4e79;
        border-radius: 8px;
        padding: 1rem 1.2rem;
        margin: 0.5rem 0;
    }
    .hadith-card .source {
        font-size: 0.75rem;
        color: #888;
        margin-bottom: 0.3rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .hadith-card .text { color: #222; line-height: 1.8; font-size: 0.95rem; }
    .hadith-card .arabic {
        color: #1f4e79;
        font-size: 1.1rem;
        text-align: right;
        direction: rtl;
        margin-top: 0.5rem;
        font-family: 'Traditional Arabic', serif;
        line-height: 2;
    }
    .metric-box {
        background: #1f4e79;
        color: white;
        border-radius: 8px;
        padding: 0.8rem;
        text-align: center;
        margin: 0.3rem 0;
    }
    .metric-box .num { font-size: 1.5rem; font-weight: 700; }
    .metric-box .label { font-size: 0.7rem; opacity: 0.8; text-transform: uppercase; }
    .stChatMessage { border-radius: 12px; }
    .score-badge {
        display: inline-block;
        background: #e8f4e8;
        color: #2d7a2d;
        border-radius: 99px;
        padding: 2px 10px;
        font-size: 0.75rem;
        font-weight: 600;
        margin-left: 8px;
    }
    .tag {
        display: inline-block;
        background: #e8f0f8;
        color: #1f4e79;
        border-radius: 4px;
        padding: 2px 8px;
        font-size: 0.7rem;
        margin: 2px;
        font-weight: 500;
    }
    footer { display: none; }
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="main-header">
    <h1>☪️ Hadith Information Retrieval System</h1>
    <p>Entity-Aware RAG Pipeline · NLP · Named Entity Recognition · Fuzzy Matching</p>
    <p style="font-size:0.8rem;color:#888">Portfolio project by <strong>Nurul Najwa Norhisham</strong> · 
    <a href="https://ieeexplore.ieee.org/document/11488814" target="_blank">IEEE Published Research</a></p>
</div>
""", unsafe_allow_html=True)

# ── Initialize RAG ─────────────────────────────────────────────────────────────
@st.cache_resource(show_spinner="Loading Hadith knowledge base...")
def load_rag():
    api_key = os.environ.get("GOOGLE_API_KEY", st.secrets.get("GOOGLE_API_KEY", ""))
    return HadithRAG(api_key=api_key)

rag = load_rag()

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🏗️ Architecture")
    st.markdown("""
    This system implements an **Entity-Aware RAG pipeline**:
    
    1. **NER** — extracts Islamic entities (prophets, companions, topics)
    2. **Fuzzy Matching** — handles Arabic name variations
    3. **Vector Search** — semantic similarity via ChromaDB
    4. **LLM Generation** — Gemini synthesises final answer
    """)

    st.divider()
    st.markdown("### 📊 Knowledge Base Stats")
    stats = rag.get_stats()
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""<div class="metric-box">
            <div class="num">{stats['total_hadiths']}</div>
            <div class="label">Hadiths</div>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown(f"""<div class="metric-box">
            <div class="num">{stats['collections']}</div>
            <div class="label">Collections</div>
        </div>""", unsafe_allow_html=True)

    st.divider()
    st.markdown("### 🔍 Retrieval Settings")
    top_k = st.slider("Results to retrieve", 1, 10, 5)
    use_fuzzy = st.toggle("Enable fuzzy matching", value=True)
    use_ner = st.toggle("Enable NER extraction", value=True)

    st.divider()
    st.markdown("### 💡 Example Questions")
    examples = [
        "What does Islam say about kindness to parents?",
        "Hadith about cleanliness",
        "What did Prophet Muhammad say about patience?",
        "Hadith on seeking knowledge",
        "What are the rights of neighbours in Islam?",
    ]
    for ex in examples:
        if st.button(ex, key=ex, use_container_width=True):
            st.session_state.example_query = ex

    st.divider()
    st.markdown("""
    <div style="font-size:0.7rem;color:#888;text-align:center">
    Built with Python · ChromaDB · Gemini API<br>
    Based on IEEE-published FYP research<br>
    <a href="https://github.com/Nurul-Najwa-N" target="_blank">github.com/Nurul-Najwa-N</a>
    </div>
    """, unsafe_allow_html=True)

# ── Chat Interface ─────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "assistant",
        "content": "As-salamu alaykum! 🌙 I'm a Hadith retrieval assistant built with an Entity-Aware RAG pipeline. Ask me anything about Islamic teachings from authentic Hadith collections (Sahih Bukhari, Sahih Muslim, Abu Dawud, Tirmidhi, and more).\n\nTry asking: *\"What did the Prophet say about honesty?\"*"
    })

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"], unsafe_allow_html=True)
        if "hadiths" in msg:
            st.markdown("**📖 Retrieved Hadiths:**")
            for h in msg["hadiths"]:
                st.markdown(f"""
                <div class="hadith-card">
                    <div class="source">{h['collection']} · {h['reference']}
                        <span class="score-badge">Score: {h['score']:.2f}</span>
                    </div>
                    <div class="text">{h['text']}</div>
                    {'<div class="arabic">' + h['arabic'] + '</div>' if h.get('arabic') else ''}
                </div>
                """, unsafe_allow_html=True)
            if msg.get("entities"):
                st.markdown("**🏷️ Entities detected:** " + " ".join([f'<span class="tag">{e}</span>' for e in msg["entities"]]), unsafe_allow_html=True)

# Handle example button click
if "example_query" in st.session_state:
    query = st.session_state.pop("example_query")
    st.session_state.pending_query = query

# Chat input
query = st.chat_input("Ask about any Islamic teaching or Hadith topic...")
if "pending_query" in st.session_state:
    query = st.session_state.pop("pending_query")

if query:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Retrieving relevant Hadiths..."):
            result = rag.query(
                query=query,
                top_k=top_k,
                use_fuzzy=use_fuzzy,
                use_ner=use_ner
            )

        # Show retrieved hadiths
        if result["hadiths"]:
            st.markdown("**📖 Retrieved Hadiths:**")
            for h in result["hadiths"]:
                st.markdown(f"""
                <div class="hadith-card">
                    <div class="source">{h['collection']} · {h['reference']}
                        <span class="score-badge">Score: {h['score']:.2f}</span>
                    </div>
                    <div class="text">{h['text']}</div>
                    {'<div class="arabic">' + h['arabic'] + '</div>' if h.get('arabic') else ''}
                </div>
                """, unsafe_allow_html=True)

        if result.get("entities"):
            st.markdown("**🏷️ Entities detected:** " + " ".join([f'<span class="tag">{e}</span>' for e in result["entities"]]), unsafe_allow_html=True)

        # Show AI answer
        st.markdown("---")
        st.markdown(result["answer"])

        # Store in session
        st.session_state.messages.append({
            "role": "assistant",
            "content": result["answer"],
            "hadiths": result["hadiths"],
            "entities": result.get("entities", [])
        })
