from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..auth import oauth2
from ..db.session import get_db
from ..repository import rolerepo, userrepo
from ..schemas import roleschema, userschema

router = APIRouter(
    prefix="/roles",
    tags=['roles']
)

unauthorized_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="You are unauthorized to access this resource!",
    headers={"WWW-Authenticate": "Bearer"},
)


@router.get("", response_model=List[roleschema.RoleOut])
def get_all(db: Session = Depends(get_db), current_user_email: userschema.UserIn = Depends(oauth2.get_current_user_email)):
    current_user = userrepo.get_one_token(current_user_email, db)
    if current_user.role == 1:
        return rolerepo.get_all(db)
    raise unauthorized_exception


@router.get("/{id}", response_model=roleschema.RoleOut)
def get_one(id: int, db: Session = Depends(get_db), current_user_email: userschema.UserIn = Depends(oauth2.get_current_user_email)):
    current_user = userrepo.get_one_token(current_user_email, db)
    if current_user.role == 1:
        return rolerepo.get_one(id, db)
    raise unauthorized_exception


@router.post("", response_model=roleschema.RoleOut)
def create(request: roleschema.RoleIn, db: Session = Depends(get_db), current_user_email: userschema.UserIn = Depends(oauth2.get_current_user_email)):
    current_user = userrepo.get_one_token(current_user_email, db)
    if current_user.role == 1:
        return rolerepo.create(request, db)
    raise unauthorized_exception


@router.put("/{id}", response_model=roleschema.RoleOut)
def update(id: int, request: roleschema.RoleUpdate, db: Session = Depends(get_db), current_user_email: userschema.UserIn = Depends(oauth2.get_current_user_email)):
    current_user = userrepo.get_one_token(current_user_email, db)
    if current_user.role == 1:
        return rolerepo.update(id, request, db)
    raise unauthorized_exception


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db), current_user_email: userschema.UserIn = Depends(oauth2.get_current_user_email)):
    current_user = userrepo.get_one_token(current_user_email, db)
    if current_user.role == 1:
        return rolerepo.destroy(id, db)
    raise unauthorized_exception

