from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.regulation import Regulation
from app.schemas.regulation import RegulationCreate, RegulationResponse
from app.crud.regulation import create_regulation as create_regulation_db
from app.crud.regulation import (
    create_regulation as create_regulation_db,
    get_regulations
)

router = APIRouter(
    prefix="/regulations",
    tags=["Regulations"]
)


@router.post("/", response_model=RegulationResponse)
def create_regulation(
    regulation: RegulationCreate,
    db: Session = Depends(get_db)
):
    return create_regulation_db(db, regulation.name)
@router.get("/", response_model=list[RegulationResponse])
def read_regulations(
    db: Session = Depends(get_db)
):
    return get_regulations(db)