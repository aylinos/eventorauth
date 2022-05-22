from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ..auth import oauth2
from ..db.session import get_db
from ..repository import userrepo
from ..schemas import userschema

router = APIRouter(
    prefix="/user",
    tags=['users']
)


@router.get("/", response_model=List[userschema.UserOut])
def get_all_users(db: Session = Depends(get_db), current_user: userschema.UserIn = Depends(oauth2.get_current_user)):
    return userrepo.get_all(db)


@router.get("/{id}", response_model=userschema.UserOut)
def get_one_user(id: int, db: Session = Depends(get_db), current_user: userschema.UserIn = Depends(oauth2.get_current_user)):
    return userrepo.get_one(id, db)


@router.get("/me", response_model=userschema.UserOut)
async def read_users_me(current_user: userschema.UserIn = Depends(oauth2.get_current_user)):
    return current_user


# User Signup [ Create a new user ]
@router.post("/signup", response_model=userschema.UserOut)
def user_signup(request: userschema.UserIn, db: Session = Depends(get_db)):
    return userrepo.create(request, db)


@router.put("/{id}", response_model=userschema.UserOut)
def update_user(id: int, request: userschema.UserUpdate, db: Session = Depends(get_db)):
    return userrepo.update(id, request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy_user(id: int, db: Session = Depends(get_db)):
    return userrepo.destroy(id, db)
