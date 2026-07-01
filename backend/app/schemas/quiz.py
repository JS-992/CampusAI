from pydantic import BaseModel
from typing import List


class QuizRequest(BaseModel):
    subject: str


class QuizQuestion(BaseModel):
    question: str
    options: List[str]
    answer: str


class QuizResponse(BaseModel):
    quiz: List[QuizQuestion]