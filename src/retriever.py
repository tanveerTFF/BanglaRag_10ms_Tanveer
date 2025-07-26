# src/retriever.py

from sentence_transformers import SentenceTransformer
from chromadb import PersistentClient
from src.config import VECTOR_DB_DIR, EMBED_MODEL_NAME


def retrieve_similar_chunks(query: str, top_k: int = 3) -> list:
    # 1. Load the same embedding model
    model = SentenceTransformer(EMBED_MODEL_NAME)

    # 2. Connect to existing ChromaDB
    client = PersistentClient(path=VECTOR_DB_DIR)
    collection = client.get_or_create_collection("bangla_rag")

    # 3. Embed the user query
    query_embedding = model.encode(query, normalize_embeddings=True).tolist()

    # 4. Perform similarity search in ChromaDB
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=["documents", "distances"]
    )

    # 5. Extract top documents and distances
    retrieved_chunks = results["documents"][0]
    distances = results["distances"][0]

    print(f"\n🔍 Top {top_k} retrieved chunks for query: {query}")
    for i, (chunk, dist) in enumerate(zip(retrieved_chunks, distances), start=1):
        print(f"\n--- Chunk {i} (distance: {dist:.4f}) ---\n{chunk.strip()}")

    return retrieved_chunks


if __name__ == "__main__":
    while True:
        user_input = input("\n📝 Enter your query (or type 'exit' to quit):\n> ")
        if user_input.strip().lower() == "exit":
            break
        retrieve_similar_chunks(user_input)
