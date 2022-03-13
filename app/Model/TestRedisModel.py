from redis_om import HashModel
from app.Config.config import Config


class TestRedisModel(HashModel):
    name: str
    age: int

    class Meta:
        database = Config.RedisConf.redis_db

