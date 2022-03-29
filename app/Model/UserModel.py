from pydantic import BaseModel
from typing import Union, List


class UserModel(BaseModel):
    email: Union[str, None]
    password: Union[str, None]
    name: Union[str, None]
    lastname: Union[str, None]


class UserResponseModel(BaseModel):
    data: Union[List[UserModel], None]
    success: Union[bool, None]
