from fastapi import APIRouter, UploadFile, File, Form, Depends
from sqlalchemy.orm import Session
import os
import shutil

from app.database.connection import get_db
from app.crud.material import create_material
from app.schemas.material import MaterialResponse


router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)


UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/", response_model=MaterialResponse)
def upload_file(
    file: UploadFile = File(...),
    title: str = Form(...),
    subject_id: int = Form(...),
    db: Session = Depends(get_db)
):

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    file_type = file.content_type

    material = create_material(
        db=db,
        title=title,
        file_name=file.filename,
        file_path=file_path,
        file_type=file_type,
        subject_id=subject_id
    )

    return material