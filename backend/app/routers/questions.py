from fastapi import APIRouter
from app.schemas.questions import QuestionRequest

router = APIRouter()

@router.post("/questions")
async def generate_questions(request: QuestionRequest):

    return {
        "questions": [
            f"What is covered in {request.chapter}?",
            f"Explain the main concepts of {request.chapter}.",
            f"List three important points from {request.chapter}."
        ]
    }