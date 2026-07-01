from fastapi import FastAPI
from app.routers import upload
from app.routers import summary
from app.routers import chat
from app.routers import questions
from app.routers import quiz
from app.config import settings

app = FastAPI(

    title=settings.APP_NAME,

    version=settings.APP_VERSION

)
@app.get("/")
def root():
    return {
        "message": "CampusAI Backend Running"
    }
app.include_router(upload.router)
app.include_router(summary.router)
app.include_router(chat.router)
app.include_router(questions.router)
app.include_router(quiz.router)