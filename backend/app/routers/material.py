from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.crud.material import get_materials_by_subject
from app.schemas.material import MaterialResponse


router = APIRouter(
    prefix="/materials",
    tags=["Materials"]
)


@router.get(
    "/subject/{subject_id}",
    response_model=list[MaterialResponse]
)
def read_materials_by_subject(
    subject_id: int,
    db: Session = Depends(get_db)
):
    return get_materials_by_subject(
        db,
        subject_id
    )