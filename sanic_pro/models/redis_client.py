import redis
from config.configs import redis_host, redis_port


class RedisClient():
    def __init__(self):
        self.conn = redis.StrictRedis(host=redis_host, port=redis_port)

#
# red = RedisClient()
# red = redis.StrictRedis(host=redis_host, port=redis_port)
# red.zadd("1", "123", "345667")