# src/ocr_loader.py

import os
from pdf2image import convert_from_path
import pytesseract
from tqdm import tqdm
from src.config import PDF_PATH, TESSERACT_PATH
import json

from langchain.text_splitter import RecursiveCharacterTextSplitter

# Set path to tesseract executable
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def ocr_extract_text_from_pdf(dpi=300):
    print("🖼️ Converting PDF to images...")
    images = convert_from_path(PDF_PATH, dpi=dpi)

    print("🔎 Running OCR on each page...")
    full_text = ""
    for image in tqdm(images):
        text = pytesseract.image_to_string(image, lang="ben")
        full_text += text + "\n"

    return full_text

def chunk_text(text, chunk_size=500, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
    )
    return splitter.split_text(text)

def load_ocr_chunks():
    text = ocr_extract_text_from_pdf()
    chunks = chunk_text(text)

    return chunks

def save_chunks_to_json(chunks, output_path="data/ocr_chunks.json"):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    chunks = load_ocr_chunks()
    print(f"\n✅ Total OCR chunks: {len(chunks)}")

    # Save to JSON for reuse
    save_chunks_to_json(chunks)

    # Optional: Preview first few
    for i, chunk in enumerate(chunks[:5]):
        print(f"\n--- Chunk {i+1} ---\n{chunk}\n")
