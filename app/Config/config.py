from redis_om import get_redis_connection


class Config:

    class MySqlConf:
        host = "mysql"
        port = "3306"
        user = "root"
        password = "Piotrek120"
        database = "ecommerce"

    class RedisConf:
        redis_db = get_redis_connection(
            host='redis',
            port=6379,
            password="Piotrek120"
        )
