from pydantic import BaseModel
from typing import Union, List


class TestModel(BaseModel):
    id: int
    name: Union[str, None]
    age: Union[int, None]


class TestResponseModel(BaseModel):
    data: Union[List[TestModel], None]
