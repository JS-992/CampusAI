from pydantic import BaseModel


class SubjectCreate(BaseModel):
    subject_name: str
    subject_code: str
    semester_id: int


class SubjectResponse(BaseModel):
    id: int
    subject_name: str
    subject_code: str
    semester_id: int

    class Config:
        from_attributes = True