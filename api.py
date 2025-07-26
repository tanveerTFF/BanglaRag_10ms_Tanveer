from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from src.generator import generate_answer
from src.retriever import retrieve_similar_chunks

app = FastAPI()
chat_history = []

class Query(BaseModel):
    question: str

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ask")
def ask_question(query: Query):
    chat_history.append(query.question)
    answer = generate_answer(query.question)
    return {"answer": answer, "history": chat_history[-5:]}
