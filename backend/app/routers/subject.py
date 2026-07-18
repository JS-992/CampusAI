from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.schemas.subject import (
    SubjectCreate,
    SubjectResponse
)

from app.crud.subject import (
    create_subject,
    get_subjects
)

router = APIRouter(
    prefix="/subjects",
    tags=["Subjects"]
)


@router.post("/", response_model=SubjectResponse)
def add_subject(
    subject: SubjectCreate,
    db: Session = Depends(get_db)
):
    return create_subject(
        db,
        subject.subject_name,
        subject.subject_code,
        subject.semester_id
    )


@router.get("/", response_model=list[SubjectResponse])
def read_subjects(
    db: Session = Depends(get_db)
):
    return get_subjects(db)