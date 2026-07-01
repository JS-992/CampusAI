from fastapi import APIRouter
from app.schemas.quiz import QuizRequest, QuizResponse, QuizQuestion

router = APIRouter()


@router.post("/quiz", response_model=QuizResponse)
async def generate_quiz(request: QuizRequest):

    return QuizResponse(
        quiz=[
            QuizQuestion(
                question=f"What is {request.subject}?",
                options=[
                    "Option A",
                    "Option B",
                    "Option C",
                    "Option D"
                ],
                answer="Option A"
            ),
            QuizQuestion(
                question=f"Which law is important in {request.subject}?",
                options=[
                    "Law 1",
                    "Law 2",
                    "Law 3",
                    "Law 4"
                ],
                answer="Law 2"
            )
        ]
    )