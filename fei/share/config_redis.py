"""config for redis
   redis相关配置，都作为os 的环境变量
   在生成docker container的时候，需要配置
   这些敏感信息也不能放到repo中，即使是私有的repo也不建议放
"""
import os
import redis

REDIS_LOCATION = os.getenv("env_redis_location")

# 测试用的redis，使用统一的password
# redis port & db: set default to 0 
REDIS_HOST = os.environ.get("redis_host")
REDIS_PORT = int(os.environ.get("redis_port", 0))
REDIS_DB = int(os.environ.get("redis_db", 0))
REDIS_PASSWORD_ALL = os.environ.get("redis_password")

# redis for rate_limit
redis_rate_limit = redis.Redis(
   host=REDIS_HOST,
   db=5,
   port=REDIS_PORT,
   password=REDIS_PASSWORD_ALL
)
