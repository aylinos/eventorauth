from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..auth import oauth2
from ..db.session import get_db
from ..repository import userrepo
from ..schemas import userschema

router = APIRouter(
    prefix="/users",
    tags=['users']
)

unauthorized_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="You are unauthorized to access this resource!",
    headers={"WWW-Authenticate": "Bearer"},
)


@router.get("/id")
def get_current_user_email(db: Session = Depends(get_db), current_user_email: userschema.UserIn = Depends(oauth2.get_current_user_email)):
    return userrepo.get_by_email(current_user_email, db).id


@router.get("", response_model=List[userschema.UserOut])
def get_all_users(db: Session = Depends(get_db), current_user_email: userschema.UserIn = Depends(oauth2.get_current_user_email)):
    return userrepo.get_all(db)


@router.get("/me", response_model=userschema.UserOut)
async def get_user_me(current_user_email: userschema.UserIn = Depends(oauth2.get_current_user_email), db: Session = Depends(get_db)):
    current_user = userrepo.get_one_token(current_user_email, db)
    return current_user


@router.get("/{id}", response_model=userschema.UserOut)
def get_one_user(id: int, db: Session = Depends(get_db), current_user_email: userschema.UserIn = Depends(oauth2.get_current_user_email)):
    return userrepo.get_one(id, db)


# User Signup [ Create a new user ]
@router.post("/signup", response_model=userschema.UserOut)
def user_signup(request: userschema.UserIn, db: Session = Depends(get_db)):
    return userrepo.create(request, db)


@router.put("/updaterole/{id}", response_model=userschema.UserOut)
def update_user_role(id:int, request: userschema.UserRoleUpdate, db: Session = Depends(get_db), current_user_email: userschema.UserIn = Depends(oauth2.get_current_user_email)):
    current_user = userrepo.get_one_token(current_user_email, db)
    if current_user.role == 1:
        return userrepo.update_user_role(id, request, db)
    raise unauthorized_exception


@router.put("/{id}", response_model=userschema.UserOut)
def update_user(id: int, request: userschema.UserUpdate, db: Session = Depends(get_db), current_user_email: userschema.UserIn = Depends(oauth2.get_current_user_email)):
    current_user = userrepo.get_one_token(current_user_email, db)
    if current_user.id == id or current_user.role == 1:
        return userrepo.update(id, request, db)
    raise unauthorized_exception


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy_user(id: int, db: Session = Depends(get_db), current_user_email: userschema.UserIn = Depends(oauth2.get_current_user_email)):
    current_user = userrepo.get_one_token(current_user_email, db)
    if current_user.id == id or current_user.role == 1:
        return userrepo.destroy(id, db)
    raise unauthorized_exception



