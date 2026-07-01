from fastapi import APIRouter
from app.schemas.chat import ChatRequest

router = APIRouter()

@router.post("/chat")
async def chat(data: ChatRequest):

    return {
        "answer": f"Dummy answer for: {data.question}"
    }