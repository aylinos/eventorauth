# Pydantic model(s): properties required during user creation & login
from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    name: str = Field(default=None)
    email: str = Field(default=None)
    password: str = Field(default=None)

    class Config:
        the_schema = {
            "user_demo": {
                "name": "User",
                "email": "user@mail.com",
                "password": "1234"
            }
        }


class UserLoginSchema(BaseModel):
    email: str = Field(default=None)
    password: str = Field(default=None)

    class Config:
        the_schema = {
            "user_demo": {
                "email": "user@mail.com",
                "password": "1234"
            }
        }
