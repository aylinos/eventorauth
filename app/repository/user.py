from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.auth.hashing import Hash
from app.models import user
from app.schemas import userschema


def get_all(db: Session):
    users = db.query(user.User).all()
    return users


def get_one(id: int, db: Session):
    found_user = db.query(user.User).filter(user.User.id == id).first()
    if not found_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {id} is not available")
    return found_user


def create(request: userschema.UserBase, db:Session):
    new_user = user.User(name=request.name, email=request.email, hashed_password=Hash.bcrypt(request.hashed_password),
                         role=2)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
