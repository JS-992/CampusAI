from fastapi import APIRouter
from app.schemas.summary import SummaryRequest

router = APIRouter()


@router.post("/summarize")
async def summarize(data: SummaryRequest):

    return {
        "summary": f"This is a dummy summary for {data.subject}."
    }