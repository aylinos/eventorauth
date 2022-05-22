from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from ..auth.hashing import Hash
from ..models import user
from ..schemas import userschema


def get_all(db: Session):
    users = db.query(user.User).all()
    return users


def get_one(id: int, db: Session):
    found_user = db.query(user.User).filter(user.User.id == id).first()
    if not found_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {id} is not available")
    return found_user


def create(request: userschema.UserIn, db: Session):
    new_user = user.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password),
                         role=2)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def update(id: int, request: userschema.UserUpdate, db: Session):
    found_user = db.query(user.User).filter(user.User.id == id)

    if not found_user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} not found")

    # Check if user from cookie is the same as creator in found_event or is admin
    found_user.update(request.dict(exclude_unset=True))
    db.commit()
    return found_user.first()


def destroy(id: int, db: Session):
    found_user = db.query(user.User).filter(user.User.id == id)

    if not found_user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} not found")

    # Check if user from cookie is the same as creator in found_event or is admin
    found_user.delete(synchronize_session=False)
    db.commit()
    return True
