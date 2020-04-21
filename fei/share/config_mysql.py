"""config for mysql database
   mysql的相关配置，都作为os 的环境变量
   在生成docker container的时候，需要配置
   这些敏感信息也不能放到repo中，即使是私有的repo也不建议放
"""
import os

from os import getenv

DATABASES_MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': os.getenv('env_db_host'),
        'NAME': os.getenv('env_db_database'),
        'USER': os.getenv('env_db_user'),
        'PASSWORD': os.getenv('env_db_password'),
        'PORT': os.getenv('env_db_port'),
        'CONN_MAX_AGE': 27800,
        'OPTIONS': {
            'autocommit': True,
        },
    },
    'OPTIONS': {
        'timeout': 26000,
    }
}
