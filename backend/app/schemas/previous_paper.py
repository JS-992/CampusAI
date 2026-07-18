from pydantic import BaseModel


class PreviousPaperCreate(BaseModel):
    year: int
    exam_type: str
    file_path: str
    subject_id: int


class PreviousPaperResponse(BaseModel):
    id: int
    year: int
    exam_type: str
    file_path: str
    subject_id: int

    class Config:
        from_attributes = True