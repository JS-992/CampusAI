from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.database.connection import Base


class DocumentChunk(Base):

    __tablename__ = "document_chunks"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    material_id = Column(
        Integer,
        ForeignKey("materials.id"),
        nullable=False
    )

    chunk_index = Column(
        Integer,
        nullable=False
    )

    chunk_text = Column(
        Text,
        nullable=False
    )

    material = relationship(
        "Material",
        back_populates="chunks"
    )