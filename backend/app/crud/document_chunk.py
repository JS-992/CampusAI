from sqlalchemy.orm import Session

from app.models.document_chunk import DocumentChunk


def get_chunks_by_material(db: Session, material_id: int):
    return (
        db.query(DocumentChunk)
        .filter(DocumentChunk.material_id == material_id)
        .order_by(DocumentChunk.chunk_index)
        .all()
    )