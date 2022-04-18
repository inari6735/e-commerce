from pydantic import BaseModel
from redis_om import JsonModel, EmbeddedJsonModel
from app.Config.config import Config
from app.Model.ProductModel import ProductModel
from typing import Union, List


class ProductRedisModel(EmbeddedJsonModel, ProductModel):
    class Meta:
        database = Config.RedisConf.redis_db


class CartRedisModel(JsonModel):
    product: Union[List[ProductRedisModel], None]

    class Meta:
        database = Config.RedisConf.redis_db


class CartRedisResponseModel(BaseModel):
    data: Union[CartRedisModel, None]
    success: Union[bool, None]
