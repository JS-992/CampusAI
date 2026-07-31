from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.services.vector_store.index_service import index_material

router = APIRouter(
    prefix="/index-material",
    tags=["Index Material"]
)


@router.post("/{material_id}")
def index(material_id: int, db: Session = Depends(get_db)):
    count = index_material(db, material_id)

    return {
        "message": "Material indexed successfully",
        "chunks_indexed": count
    }