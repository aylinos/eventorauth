from typing import List

from pydantic import BaseModel


# Pydantic model: properties required during role creation
class Role(BaseModel):
    title: str


# Properties to receive via API on update
class RoleUpdate(Role):
    ...


class ShowRole(Role):
    users: List

    class Config:
        orm_mode = True
