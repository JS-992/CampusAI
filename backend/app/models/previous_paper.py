from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database.connection import Base


class PreviousPaper(Base):
    __tablename__ = "previous_papers"

    id = Column(Integer, primary_key=True, index=True)

    year = Column(Integer, nullable=False)

    exam_type = Column(String, nullable=False)

    file_path = Column(String, nullable=False)

    subject_id = Column(
        Integer,
        ForeignKey("subjects.id"),
        nullable=False
    )

    subject = relationship(
        "Subject",
        back_populates="previous_papers"
    )