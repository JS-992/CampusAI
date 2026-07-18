from sqlalchemy.orm import Session
from app.models.semester import Semester


def create_semester(
    db: Session,
    semester_no: int,
    regulation_id: int
):
    semester = Semester(
        semester_no=semester_no,
        regulation_id=regulation_id
    )

    db.add(semester)
    db.commit()
    db.refresh(semester)

    return semester


def get_semesters(db: Session):
    return db.query(Semester).all()