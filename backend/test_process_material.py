from app.database.connection import SessionLocal
from app.services.document_processing.document_service import (
    process_material
)


db = SessionLocal()

try:
    result = process_material(
        db=db,
        material_id=2
    )

    print(result)

finally:
    db.close()