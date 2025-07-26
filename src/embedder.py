# src/embedder.py

from sentence_transformers import SentenceTransformer
from chromadb import PersistentClient
import json
import os

from src.config import VECTOR_DB_DIR, EMBED_MODEL_NAME

def load_and_prepare_chunks():
    with open("data/ocr_chunks.json", "r", encoding="utf-8") as f:
        return json.load(f)

def embed_and_store_chunks():
    # 1. Load model
    model = SentenceTransformer(EMBED_MODEL_NAME)

    # 2. Load OCR-prepared chunks
    chunks = load_and_prepare_chunks()

    # 3. Set up persistent Chroma client
    chroma_client = PersistentClient(path=VECTOR_DB_DIR)

    # 4. Drop old collection if exists
    if "bangla_rag" in [col.name for col in chroma_client.list_collections()]:
        chroma_client.delete_collection("bangla_rag")

    # 5. Create new clean collection
    collection = chroma_client.get_or_create_collection(name="bangla_rag")

    # 6. Embed and store
    for i, chunk in enumerate(chunks):
        embedding = model.encode(chunk, normalize_embeddings=True).tolist()
        collection.add(
            documents=[chunk],
            embeddings=[embedding],
            ids=[f"chunk-{i}"]
        )

    print(f"✅ Stored {len(chunks)} chunks in ChromaDB.")

if __name__ == "__main__":
    embed_and_store_chunks()
