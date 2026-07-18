from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.database.connection import Base


class Semester(Base):
    __tablename__ = "semesters"

    id = Column(Integer, primary_key=True, index=True)

    semester_no = Column(Integer, nullable=False)

    regulation_id = Column(
        Integer,
        ForeignKey("regulations.id"),
        nullable=False
    )

    regulation = relationship(
        "Regulation",
        back_populates="semesters"
    )
    subjects = relationship(
    "Subject",
    back_populates="semester",
    cascade="all, delete"
)