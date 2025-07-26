# src/config.py

import os

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(__file__)) #location of config fioler
DATA_DIR = os.path.join(BASE_DIR, "data")
PDF_PATH = os.path.join(DATA_DIR, "HSC26-Bangla1st-Paper.pdf") #input pdf file
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# Chroma settings
VECTOR_DB_DIR = os.path.join(BASE_DIR, "chroma_db") #vector index stored here

# Chunking
CHUNK_SIZE = 300 #spilitting full text into 300 char long chunks
CHUNK_OVERLAP = 50 #50 vharacter overlap in between chunks to ensure contunuity

# Embedding model

EMBED_MODEL_NAME = "BAAI/bge-m3" #model used for embedding

# EMBED_MODEL_NAME = "intfloat/multilingual-e5-small"

#EMBED_MODEL_NAME = "ibm-granite/granite-embedding-278m-multilingual"


if __name__ == "__main__":
    print("Tesseract Path:", TESSERACT_PATH)
    print("PDF Path:", PDF_PATH)
