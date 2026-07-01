from pydantic import BaseModel

class QuestionRequest(BaseModel):
    chapter: str