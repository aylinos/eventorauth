from sqlalchemy.orm import Session

from app.models import role


def get_all(db: Session):
    roles = db.query(role.Role).all()
    return roles