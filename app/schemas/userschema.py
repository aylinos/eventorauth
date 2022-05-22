from pydantic import BaseModel


# Pydantic model: properties required during user creation
class UserBase(BaseModel):
    name: str
    email: str
    hashed_password: str
    # role: int


# Properties to receive via API on update
class UserUpdate(UserBase):
    ...


class ShowUser(BaseModel):
    name: str
    email: str
    # user_role: ShowRole

    class Config:
        orm_mode = True


class Login(BaseModel):
    email: str
    hashed_password: str
