from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth import oauth2
from app.db.session import get_db
from app.models import role
from app.repository import role
from app.schemas import roleschema, userschema

router = APIRouter(
    prefix="/role",
    tags=['roles']
)


@router.get("/", response_model=List[roleschema.ShowRole])
def get_role(db: Session = Depends(get_db), current_user: userschema.UserBase = Depends(oauth2.get_current_user)):
    return role.get_all(db)
