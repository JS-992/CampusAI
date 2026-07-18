from sqlalchemy.orm import Session

from app.models.subject import Subject


def create_subject(
    db: Session,
    subject_name: str,
    subject_code: str,
    semester_id: int
):
    subject = Subject(
        subject_name=subject_name,
        subject_code=subject_code,
        semester_id=semester_id
    )

    db.add(subject)
    db.commit()
    db.refresh(subject)

    return subject


def get_subjects(db: Session):
    return db.query(Subject).all()