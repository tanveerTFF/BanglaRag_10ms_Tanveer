![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-%E2%9A%A1-red)
![FastAPI](https://img.shields.io/badge/API-FastAPI-green)


# Bangla Literature RAG Assistant 

A multilingual Retrieval-Augmented Generation (RAG) system that understands **Bangla and English** queries, retrieves relevant passages from a Bangla literature PDF (HSC 1st Paper), and generates precise answers using a local LLM. Built as part of the AI Engineer (Level-1) assessment.

---

## ✨ Features

- ✅ Accepts queries in English & Bangla
- 📄 Uses OCR to extract Bangla textbook content
- 🔎 Stores knowledge as vector embeddings (ChromaDB)
- 💡 Answers grounded in retrieved context using Ollama (`llama3`)
- 🧠 Continuous chat memory (Streamlit chatbot)
- 📊 Similarity score visualization for evaluation
- 🌐 REST API using FastAPI

---

## 🖼 Sample Questions

| Question (Bangla)                                        | Answer         |
|----------------------------------------------------------|----------------|
| অনুপমের ভাষায় সুপুরুষ কাকে বলা হয়েছে?                   | শম্ভুনাথ       
| কাকে অনুপমের ভাগ্যদেবতা বলে উল্লেখ করা হয়েছে?            | মামা          
| বিয়ের সময় কল্যাণীর প্রকৃত বয়স কত ছিল?                   | ১৫ বছর        

---

## 🚀 Quick Start

### 1. Clone & Setup Environment

```bash
git clone https://github.com/your-username/rag-10ms.git
cd rag-10ms
python -m venv .venv
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
.venv\Scripts\activate  # (Windows)

2. Install Requirements

pip install --upgrade pip
pip install -r requirements.txt

3. Run the program

go to your rag-10ms directory
run in terminal uvicorn api:app --reload
you should see 👋 generator.py has started
now open another terminal
run streamlit run chat_app.py

streamlit will open and you can ask questions!




🛠️ Tools & Libraries Used

🔤 pytesseract + pdf2image — OCR on scanned Bangla PDF

🧠 sentence-transformers — Embeddings using ibm-granite/multilingual

📦 chromadb — Vector database for long-term memory

🔗 ollama — Local LLM (LLaMA3)

🌐 FastAPI — REST API for serving answers

🧪 Streamlit — UI chatbot with memory

📊 matplotlib — Similarity score evaluation
