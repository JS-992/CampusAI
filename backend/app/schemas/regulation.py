from pydantic import BaseModel


class RegulationCreate(BaseModel):
    name: str


class RegulationResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True