# src/loader.py

import fitz  # PyMuPDF
import re
from typing import List
from src.config import PDF_PATH, CHUNK_SIZE, CHUNK_OVERLAP

def extract_text_from_pdf(path: str) -> str:
    """Extract raw text from a Bangla PDF using PyMuPDF."""
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def clean_bangla_text(text: str) -> str:
    """Clean and normalize Bangla text (remove junk characters)."""
    # Keep only Bangla chars, digits, and basic punctuation
    text = re.sub(r'[^\u0980-\u09FF\s.,?!]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra whitespace
    return text


def chunk_text(text: str, chunk_size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> List[str]:
    """Split text into overlapping chunks for embedding."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks


def load_and_prepare_chunks() -> List[str]:
    """Main function to load PDF, clean, chunk and return ready-to-embed text chunks."""
    raw_text = extract_text_from_pdf(PDF_PATH)
    cleaned_text = clean_bangla_text(raw_text)
    chunks = chunk_text(cleaned_text)
    return chunks
