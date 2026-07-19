from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.services.document_processing.document_service import (
    process_material as process_material_service
)


router = APIRouter(
    prefix="/process-material",
    tags=["Document Processing"]
)


@router.post("/{material_id}")
def process_material(
    material_id: int,
    db: Session = Depends(get_db)
):

    try:

        return process_material_service(
            db,
            material_id
        )

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )