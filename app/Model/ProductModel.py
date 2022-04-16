from pydantic import BaseModel
from typing import Union, List


class ProductModel(BaseModel):
    product_code: str
    name: Union[str, None]
    price: int
    quantity: int


class ProductResponseModel(BaseModel):
    data: Union[List[ProductModel], None]
    success: Union[bool, None]
