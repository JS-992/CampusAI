from sqlalchemy.orm import Session

from app.models.regulation import Regulation


def create_regulation(db: Session, name: str):

    regulation = Regulation(name=name)

    db.add(regulation)

    db.commit()

    db.refresh(regulation)
    

    return regulation
def get_regulations(db: Session):
    return db.query(Regulation).all()