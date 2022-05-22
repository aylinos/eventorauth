from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from ..models import role
from ..schemas import roleschema


def get_all(db: Session):
    roles = db.query(role.Role).all()
    return roles


def get_one(id: int, db: Session):
    found_role = db.query(role.Role).filter(role.Role.id == id).first()
    if not found_role:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Role with id: {id} is not available")
    return found_role


def create(request: roleschema.RoleIn, db: Session):
    # Catch title already exists exception
    new_role = role.Role(title=request.title)
    db.add(new_role)
    db.commit()
    db.refresh(new_role)
    return new_role


def update(id: int, request: roleschema.RoleUpdate, db: Session):
    # Check if user from cookie is admin
    # Catch title already exists exception
    found_role = db.query(role.Role).filter(role.Role.id == id)

    if not found_role.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Role with id {id} not found")

    if request.title:
        found_role.update(request.dict(exclude_unset=True))
        db.commit()
    return found_role.first()


def destroy(id: int, db: Session):
    # Check if user from cookie is admin
    found_role = db.query(role.Role).filter(role.Role.id == id)

    if not found_role.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Role with id {id} not found")

    found_role.delete(synchronize_session=False)
    db.commit()
    return True
