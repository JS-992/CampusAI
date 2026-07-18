from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.crud.previous_paper import create_previous_paper as create_previous_paper_db
from app.schemas.previous_paper import (
    PreviousPaperCreate,
    PreviousPaperResponse
)


router = APIRouter(
    prefix="/previous-papers",
    tags=["Previous Papers"]
)


@router.post(
    "/",
    response_model=PreviousPaperResponse
)
def add_previous_paper(
    paper: PreviousPaperCreate,
    db: Session = Depends(get_db)
):
    return create_previous_paper_db(
        db=db,
        year=paper.year,
        exam_type=paper.exam_type,
        file_path=paper.file_path,
        subject_id=paper.subject_id
    )