# streamlit_app.py

import streamlit as st
from src.generator import generate_answer

st.set_page_config(page_title="Bangla Literature QA", layout="centered")

st.title("📚 Bangla Literature RAG Assistant")
st.write("Ask a question related to Bangla literature based on your uploaded textbook!")

query = st.text_input("❓ Enter your question:")

if query:
    with st.spinner("🔍 Retrieving relevant information and generating answer..."):
        try:
            answer = generate_answer(query)
            st.markdown("### 🧠 Answer:")
            st.write(answer)
        except Exception as e:
            st.error(f"❌ Error: {e}")
