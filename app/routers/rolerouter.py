from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..auth import oauth2
from ..db.session import get_db
from ..repository import rolerepo
from ..schemas import roleschema, userschema

router = APIRouter(
    prefix="/role",
    tags=['roles']
)


@router.get("/", response_model=List[roleschema.ShowRole])
def get_role(db: Session = Depends(get_db), current_user: userschema.UserBase = Depends(oauth2.get_current_user)):
    return rolerepo.get_all(db)
