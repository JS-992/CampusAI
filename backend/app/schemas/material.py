from pydantic import BaseModel
from datetime import datetime


class MaterialResponse(BaseModel):
    id: int
    title: str
    file_name: str
    file_path: str
    file_type: str
    created_at: datetime
    subject_id: int

    class Config:
        from_attributes = True