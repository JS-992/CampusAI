from sqlalchemy.orm import Session

from app.models.material import Material


def create_material(
    db: Session,
    title: str,
    file_name: str,
    file_path: str,
    file_type: str,
    subject_id: int
):
    material = Material(
        title=title,
        file_name=file_name,
        file_path=file_path,
        file_type=file_type,
        subject_id=subject_id
    )

    db.add(material)
    db.commit()
    db.refresh(material)

    return material


def get_materials_by_subject(
    db: Session,
    subject_id: int
):
    return (
        db.query(Material)
        .filter(Material.subject_id == subject_id)
        .all()
    )