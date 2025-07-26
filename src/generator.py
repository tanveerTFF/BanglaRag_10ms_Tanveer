# src/generator.py

print("👋 generator.py has started")


import requests
from src.retriever import retrieve_similar_chunks

OLLAMA_URL = "http://localhost:11434/api/chat"
OLLAMA_MODEL = "llama3"  # Change to your preferred local model

def call_ollama(prompt: str) -> str:
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": OLLAMA_MODEL,
            "stream": False,  # 🛠️ This is the fix
            "messages": [
                {"role": "system", "content": "You are a helpful assistant for Bangla literature questions."},
                {"role": "user", "content": prompt}
            ]
        }
    )
    response.raise_for_status()
    output = response.json()
    return output["message"]["content"]


def generate_answer(question: str, top_k: int = 3) -> str:
    # 1. Retrieve top matching chunks
    chunks = retrieve_similar_chunks(question, top_k=top_k)

    # 2. Create a prompt combining chunks + question
    context = "\n\n".join(chunks)
    prompt = f"""
    তুমি একজন জ্ঞানের ভাণ্ডার বাংলা সহকারী। তোমার কাজ হলো প্রশ্নের যথাযথ এবং প্রাসঙ্গিক উত্তর দেওয়া শুধুমাত্র নিচের তথ্য ব্যবহার করে। 

    প্রশ্ন: {question}

    নিচে কিছু প্রাসঙ্গিক তথ্য OCR থেকে পাওয়া গেছে:

    {context}

    👉 উপরোক্ত তথ্যের ভিত্তিতে সংক্ষিপ্ত কিন্তু সঠিক উত্তর দাও। উত্তর বাংলায় লেখো:
    """



    # 3. Call Ollama model
    answer = call_ollama(prompt)
    return answer.strip()

if __name__ == "__main__":
    while True:
        user_input = input("\n❓ প্রশ্ন লেখো (বা 'exit' টাইপ করো বন্ধ করতে):\n> ")
        if user_input.strip().lower() == "exit":
            break

        try:
            answer = generate_answer(user_input)
            print(f"\n🧠 উত্তর:\n{answer}")
        except Exception as e:
            print(f"⚠️ Error: {e}")
