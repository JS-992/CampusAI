from sqlalchemy.orm import Session

from app.crud.document_chunk import get_chunks_by_material
from app.services.embedding.embedding_service import generate_embedding
from app.services.vector_store.chroma_service import add_chunk_to_collection
from app.services.vector_store.chroma_service import (
    delete_material_chunks
)


def index_material(db: Session, material_id: int):
    delete_material_chunks(material_id)

    chunks = get_chunks_by_material(db, material_id)

    for chunk in chunks:

        embedding = generate_embedding(chunk.chunk_text)

        add_chunk_to_collection(
            chunk_id=f"material_{material_id}_chunk_{chunk.chunk_index}",
            embedding=embedding,
            document=chunk.chunk_text,
            metadata={
                "material_id": material_id,
                "chunk_index": chunk.chunk_index
            }
        )

    return len(chunks)