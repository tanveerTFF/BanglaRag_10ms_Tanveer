# test_loader.py
from src.loader import load_and_prepare_chunks

chunks = load_and_prepare_chunks()
print(f"Total chunks: {len(chunks)}")
print("\nSample chunk:\n")
print(chunks[0])
