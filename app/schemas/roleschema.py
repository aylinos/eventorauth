from typing import List, Optional

from pydantic import BaseModel


# Pydantic model: properties required during role creation
class RoleIn(BaseModel):
    title: str


# Properties to receive via API on update
# Set the values in the model to be optional => only the field that needs to be updated can be sent
class RoleUpdate(RoleIn):
    title: Optional[str] = None


class RoleOut(RoleIn):
    id: int
    users: List

    class Config:
        orm_mode = True


class NestedRoleOut(RoleIn):
    id: int

    class Config:
        orm_mode = True
