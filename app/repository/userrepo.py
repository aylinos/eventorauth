from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from ..auth.hashing import Hash
from ..models import user
from ..schemas import userschema

notfound_exception = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                   detail=f"User not found")
already_exists_exception = HTTPException(status_code=status.HTTP_409_CONFLICT,
                                         detail=f"Email already registered")


def get_all(db: Session):
    users = db.query(user.User).all()
    return users


def get_one(id: int, db: Session):
    return find_user(id, db).first()


def get_one_token(email: str, db: Session):
    found_user = db.query(user.User).filter(user.User.email == email).first()
    if not found_user:
        raise notfound_exception
    return found_user


def create(request: userschema.UserIn, db: Session):
    found_user = db.query(user.User).filter(user.User.email == request.email).first()
    if found_user:
        raise already_exists_exception
    new_user = user.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password),
                         role=2)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def update_user_role(id: int, request: userschema.UserUpdate, db: Session):
    return updates_on_user(id, request, db)


def update(id: int, request: userschema.UserUpdate, db: Session):
    return updates_on_user(id, request, db)


def destroy(id: int, db: Session):
    found_user = find_user(id, db)
    found_user.delete(synchronize_session=False)
    db.commit()
    return True


def find_user(id: int, db: Session):
    found_user = db.query(user.User).filter(user.User.id == id)
    if not found_user.first():
        raise notfound_exception
    return found_user


def updates_on_user(id: int, request: userschema.UserUpdate, db: Session):
    found_user = find_user(id, db)
    found_user.update(request.dict(exclude_unset=True))
    db.commit()
    return found_user.first()
