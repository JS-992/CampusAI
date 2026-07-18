from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database.connection import Base


class Material(Base):
    __tablename__ = "materials"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    file_name = Column(String, nullable=False)

    file_path = Column(String, nullable=False)

    file_type = Column(String, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    subject_id = Column(
        Integer,
        ForeignKey("subjects.id"),
        nullable=False
    )

    subject = relationship(
        "Subject",
        back_populates="materials"
    )