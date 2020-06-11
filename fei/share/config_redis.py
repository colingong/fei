"""config for redis
   redis相关配置，都作为os 的环境变量
   在生成docker container的时候，需要配置
   这些敏感信息也不能放到repo中，即使是私有的repo也不建议放

   redis db:
      0: 默认
      1: 
      2:
      3:
      4: bloom filter
      5:

"""
import os
import redis
from .env_exceptions import EnvMysqlException
from .env_exceptions import EnvRedisException
from string import Template

class _RedisConfig(object):
   DEMO_ENV = os.environ.get('demo_env')
   FOR_UNITTEST = "FOR_UNITTEST"

   REDIS_LOCATION = os.environ.get("env_redis_location", FOR_UNITTEST)
   REDIS_HOST = os.environ.get("redis_host", FOR_UNITTEST)
   REDIS_PORT = int(os.environ.get("redis_port", -1))
   REDIS_DB = int(os.environ.get("redis_db", -1))
   REDIS_PASSWORD_ALL = os.environ.get("redis_password", FOR_UNITTEST)

   @classmethod
   def check_env_or_raise(cls):
      WARN_MSG = Template('====== Redis的环境变量未配置 [$env_var]\n')
      if cls.REDIS_LOCATION == cls.FOR_UNITTEST:
         print(WARN_MSG.substitute(env_var='env_redis_location'))
         raise EnvRedisException
      elif cls.REDIS_HOST == cls.FOR_UNITTEST:
         print(WARN_MSG.substitute(env_var='redis_host'))
         raise EnvRedisException
      elif cls.REDIS_PORT == -1:
         print(WARN_MSG.substitute(env_var='redis_port'))
         raise EnvRedisException
      elif cls.REDIS_DB == -1:
         print(WARN_MSG.substitute(env_var='redis_db'))
         raise EnvRedisException
      elif cls.REDIS_PASSWORD_ALL == cls.FOR_UNITTEST:
         print(WARN_MSG.substitute(env_var='redis_password'))
         raise EnvRedisException

_RedisConfig.check_env_or_raise()
# 测试用的redis，使用统一的password
# redis port & db: set default to 0 
# 如果不给默认值，readthedocs build 文档时会报错
REDIS_LOCATION = _RedisConfig.REDIS_LOCATION
REDIS_HOST = _RedisConfig.REDIS_HOST
REDIS_PORT = _RedisConfig.REDIS_PORT
REDIS_DB = _RedisConfig.REDIS_DB
REDIS_PASSWORD_ALL = _RedisConfig.REDIS_PASSWORD_ALL

# redis for rate_limit
redis_rate_limit = redis.Redis(
   host=_RedisConfig.REDIS_HOST,
   db=5,
   port=_RedisConfig.REDIS_PORT,
   password=_RedisConfig.REDIS_PASSWORD_ALL
)