from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.semester import (
    SemesterCreate,
    SemesterResponse
)
from app.crud.semester import (
    create_semester,
    get_semesters
)

router = APIRouter(
    prefix="/semesters",
    tags=["Semesters"]
)


@router.post("/", response_model=SemesterResponse)
def add_semester(
    semester: SemesterCreate,
    db: Session = Depends(get_db)
):
    return create_semester(
        db,
        semester.semester_no,
        semester.regulation_id
    )


@router.get("/", response_model=list[SemesterResponse])
def read_semesters(
    db: Session = Depends(get_db)
):
    return get_semesters(db)