from sqlalchemy.orm import Session

from app.models.previous_paper import PreviousPaper


def create_previous_paper(
    db: Session,
    year: int,
    exam_type: str,
    file_path: str,
    subject_id: int
):
    previous_paper = PreviousPaper(
        year=year,
        exam_type=exam_type,
        file_path=file_path,
        subject_id=subject_id
    )

    db.add(previous_paper)
    db.commit()
    db.refresh(previous_paper)

    return previous_paper