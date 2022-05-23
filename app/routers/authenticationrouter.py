from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ..auth.hashing import Hash
from ..auth.jwt import create_access_token
from ..db.session import get_db
from ..models import user

router = APIRouter(
    tags=['authentication']
)


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user_tolog = db.query(user.User).filter(user.User.email == request.username).first()
    if not user_tolog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid credentials")
    if not Hash.verify(user_tolog.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")

    access_token = create_access_token(data={"sub": user_tolog.email})
    return {"access_token": access_token, "token_type": "bearer"}
