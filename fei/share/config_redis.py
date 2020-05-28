"""config for redis
   redis相关配置，都作为os 的环境变量
   在生成docker container的时候，需要配置
   这些敏感信息也不能放到repo中，即使是私有的repo也不建议放
"""
import os


REDIS_LOCATION = os.getenv("env_redis_location")

# 测试用的redis，使用统一的password
REDIS_HOST = os.getenv("redis_host")
REDIS_PORT = int(os.environ.get("redis_port"))
REDIS_DB = int(os.environ.get("redis_db"))
REDIS_PASSWORD_ALL = os.getenv("redis_password")