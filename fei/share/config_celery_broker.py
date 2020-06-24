from .config_redis import REDIS_PASSWORD_ALL, REDIS_HOST, REDIS_PORT

# 'redis://:password@hostname:port/db_number'

BROKER_DB = 11
REDIS_BROKER_FOR_CELERY = f'redis://:{REDIS_PASSWORD_ALL}@{REDIS_HOST}:{REDIS_PORT}/{BROKER_DB}'