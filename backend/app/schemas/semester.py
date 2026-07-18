from pydantic import BaseModel


class SemesterCreate(BaseModel):
    semester_no: int
    regulation_id: int


class SemesterResponse(BaseModel):
    id: int
    semester_no: int
    regulation_id: int

    class Config:
        from_attributes = True