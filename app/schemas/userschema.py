from typing import Optional

from pydantic import BaseModel

from ..schemas.roleschema import NestedRoleOut


# Pydantic model: properties required during user creation
class UserIn(BaseModel):
    name: str
    email: str
    password: str


# Properties to receive via API on update
class UserUpdate(BaseModel):
    name: Optional[str]
    email: Optional[str]


# Get users from db
class UserOut(BaseModel):
    id: int
    name: str
    email: str
    role: int
    user_role: NestedRoleOut

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: str
    password: str
