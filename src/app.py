# src/app.py

from src.generator import generate_answer

def main():
    print("📚 Welcome to the Bangla Literature RAG Assistant!")
    print("Type your question below (or type 'exit' to quit).")

    while True:
        query = input("\n❓ Question:\n> ").strip()
        if query.lower() == "exit":
            print("👋 Goodbye!")
            break

        try:
            answer = generate_answer(query)
            print(f"\n🧠 Answer:\n{answer}")
        except Exception as e:
            print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    main()
