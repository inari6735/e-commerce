from pydantic import BaseModel
from typing import Union, List


class UserModel(BaseModel):
    email: str
    password: str
    name: Union[str, None]
    lastname: Union[str, None]


class UserResponseModel(BaseModel):
    data: Union[List[UserModel], None]
    success: Union[bool, None]
