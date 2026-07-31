from unittest import result

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.services.document_processing.document_service import (
    process_material as process_material_service
)
from app.services.vector_store.index_service import index_material


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

        result = process_material_service(db,
        material_id)

        indexed_chunks = index_material(db,
        material_id)

        result["indexed_chunks"] = indexed_chunks

        return result
    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )