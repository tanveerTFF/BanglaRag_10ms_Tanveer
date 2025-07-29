![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-%E2%9A%A1-red)
![FastAPI](https://img.shields.io/badge/API-FastAPI-green)


# Bangla Literature RAG Assistant 

A multilingual Retrieval-Augmented Generation (RAG) system that understands **Bangla and English** queries, retrieves relevant passages from a Bangla literature PDF (HSC 1st Paper), and generates precise answers using a local LLM.

---
📘 Project Implementation Questions & Answers

1. What method or library did you use to extract the text, and why? Did you face any formatting challenges with the PDF content?

I used pdf2image to convert PDF pages into images and pytesseract (Tesseract OCR) to extract Bangla text from each image.

This method works well for printed textbook-style content in Bangla. So In future it can be fed other textbooks that aren't in the pdf format.

Challenges faced:

The given pdf was not written in unicode so had to use ocr.

OCR occasionally misreads ligatures or special Bangla glyphs.



2. What chunking strategy did you choose (e.g., paragraph-based, sentence-based, character limit)? Why do you think it works well for semantic retrieval?
I used a character-length-based chunking strategy.

Each chunk is approximately 300–500 characters, ensuring sufficient context without being too long for the embedding model.

This approach works well for OCR content where punctuation-based splitting may be unreliable or inconsistent in Bangla.

3. What embedding model did you use? Why did you choose it? How does it capture the meaning of the text?

Model used: BAAI/bge-m3

Why:

It is a state-of-the-art multilingual embedding model supporting Bangla and optimized for dense semantic retrieval.

Performs well on noisy OCR text and both short & long queries.

How it works:

Encodes text into dense vectors using contrastive learning and multilingual pretraining, capturing semantic similarity rather than exact word overlap.

4. How are you comparing the query with your stored chunks? Why did you choose this similarity method and storage setup?

I use ChromaDB (chromadb) as the vector database and cosine similarity to compare query vectors with stored document chunk vectors.

This setup is fast, persistent, and ideal for lightweight RAG prototypes.

Cosine similarity is effective for measuring angle-based similarity in high-dimensional embedding space.

5. How do you ensure that the question and the document chunks are compared meaningfully? What would happen if the query is vague or missing context?
   
I normalize embeddings and use BAAI/bge-m3, which captures semantic intent even if the query is slightly misspelled or short.

Retrieved chunks are re-ranked by cosine distance and passed to the generator as context in the prompt.

If the query is vague or lacks context:

The generator may respond with a generic or hallucinated answer.

Solution: Better chunking, adding user clarification, or larger context windows (RAG+memory).

6. Do the results seem relevant? If not, what might improve them (e.g., better chunking, better embedding model, larger document)?
Yes, most results are relevant within the limits of the OCR data and embedding quality.

Possible improvements:

Use OpenAPI's model if there is enough budget.

Use safetensors-trained LLMs for generation.

Improve chunk cleaning (remove headings, page numbers).

Use hierarchical RAG (sections → paragraphs → sentences).

Improve OCR accuracy using Bangla-specific language post-processing.


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
git clone [https://github.com/tanveerTFF/rag-10ms.git](https://github.com/tanveerTFF/BanglaRag_10ms_Tanveer.git)
cd rag-10ms
python -m venv .venv
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
.venv\Scripts\activate  # (Windows)

2. Install Requirements

pip install --upgrade pip
pip install -r requirements.txt

3. Run the program

go to your rag-10ms directory
run in terminal : uvicorn api:app --reload
you should see  : 👋 generator.py has started
now open another terminal
run this line   : streamlit run chat_app.py

streamlit will open and you can ask questions!




🛠️ Tools & Libraries Used

🔤 pytesseract + pdf2image — OCR on scanned Bangla PDF

🧠 sentence-transformers — Embeddings using ibm-granite/multilingual

📦 chromadb — Vector database for long-term memory

🔗 ollama — Local LLM (LLaMA3)

🌐 FastAPI — REST API for serving answers

🧪 Streamlit — UI chatbot with memory

📊 matplotlib — Similarity score evaluation
