from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ..auth import oauth2
from ..db.session import get_db
from ..repository import rolerepo
from ..schemas import roleschema, userschema

router = APIRouter(
    prefix="/roles",
    tags=['roles']
)


@router.get("/", response_model=List[roleschema.RoleOut])
def get_all(db: Session = Depends(get_db), current_user: userschema.UserBase = Depends(oauth2.get_current_user)):
    return rolerepo.get_all(db)


@router.get("/{id}", response_model=roleschema.RoleOut)
def get_one(id: int, db: Session = Depends(get_db)):
    return rolerepo.get_one(id, db)


@router.post("/", response_model=roleschema.RoleOut)
def create(request: roleschema.RoleIn, db: Session = Depends(get_db)):
    return rolerepo.create(request, db)


@router.put("/{id}", response_model=roleschema.RoleOut)
def update(id: int, request: roleschema.RoleUpdate, db: Session = Depends(get_db)):
    return rolerepo.update(id, request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return rolerepo.destroy(id, db)
