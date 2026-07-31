from fastapi import APIRouter
from app.schemas.chat import ChatRequest
from app.services.rag.rag_service import ask_question

router = APIRouter()

@router.post("/")
def chat(request: ChatRequest):
    
   

    answer = ask_question(request.question)

    return {
        "answer": answer
    }