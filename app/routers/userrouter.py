from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..auth import oauth2
from ..db.session import get_db
from ..repository import userrepo
from ..schemas import userschema

router = APIRouter(
    prefix="/user",
    tags=['users']
)


@router.get("/", response_model=List[userschema.ShowUser])
def all_users(db: Session = Depends(get_db), current_user: userschema.UserBase = Depends(oauth2.get_current_user)):
    return userrepo.get_all(db)


# User Signup [ Create a new user ]
@router.post("/signup", response_model=userschema.ShowUser)
def user_signup(request: userschema.UserBase, db: Session = Depends(get_db)):
    return userrepo.create(request, db)


@router.get("/me", response_model=userschema.ShowUser)
async def read_users_me(current_user: userschema.UserBase = Depends(oauth2.get_current_user)):
    return current_user


@router.get("/{id}", response_model=userschema.ShowUser)
def get_user(id: int, db: Session = Depends(get_db), current_user: userschema.UserBase = Depends(oauth2.get_current_user)):
    return userrepo.get_one(id, db)
