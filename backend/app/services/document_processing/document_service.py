from pathlib import Path

from app.services.document_processing.pdf_processor import (
    extract_text_from_pdf
)

from app.services.document_processing.ppt_processor import (
    extract_text_from_ppt
)
from sqlalchemy.orm import Session

from app.models.material import Material
from app.models.document_chunk import DocumentChunk

from app.services.document_processing.text_cleaner import (
    clean_text
)

from app.services.document_processing.chunker import (
    split_text_into_chunks
)
from sqlalchemy import delete

def extract_text_from_document(file_path: str) -> str:
    """
    Extract text from a supported document.

    Supported formats:
    - PDF
    - PPT
    - PPTX
    """

    file_extension = Path(file_path).suffix.lower()

    if file_extension == ".pdf":
        return extract_text_from_pdf(file_path)

    elif file_extension in [".ppt", ".pptx"]:
        return extract_text_from_ppt(file_path)

    else:
        raise ValueError(
            f"Unsupported file type: {file_extension}"
        )
def process_material(
    db: Session,
    material_id: int
):
    material = (
        db.query(Material)
        .filter(Material.id == material_id)
        .first()
    )

    if not material:
        raise ValueError("Material not found")
    
    db.query(DocumentChunk).filter(
    DocumentChunk.material_id == material.id).delete(synchronize_session=False
    )

    raw_text = extract_text_from_document(
        material.file_path
    )
    
    cleaned_text = clean_text(raw_text)

    
    chunks = split_text_into_chunks(
        cleaned_text
    )
    
    for index, chunk in enumerate(chunks):

        document_chunk = DocumentChunk(
            material_id=material.id,
            chunk_index=index,
            chunk_text=chunk
        )

        db.add(document_chunk)

    db.commit()

    return {
        "material_id": material.id,
        "chunks_created": len(chunks)
    }