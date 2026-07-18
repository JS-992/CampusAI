from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database.connection import Base


class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True, index=True)

    subject_name = Column(String, nullable=False)

    subject_code = Column(String, unique=True, nullable=False)

    semester_id = Column(
        Integer,
        ForeignKey("semesters.id"),
        nullable=False
    )

    semester = relationship(
        "Semester",
        back_populates="subjects"
    )
    materials = relationship(
        "Material",
        back_populates="subject",
        cascade="all, delete"
    )
    previous_papers = relationship(
        "PreviousPaper",
        back_populates="subject",
        cascade="all, delete"
    )
    