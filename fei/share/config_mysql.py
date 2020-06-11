"""config for mysql database
   mysql的相关配置，都作为os 的环境变量
   在生成docker container的时候，需要配置
   这些敏感信息也不能放到repo中，即使是私有的repo也不建议放
"""
import os

from os import getenv

# refactory for easy testing
MYSQL_HOST = os.getenv('env_db_host')
MYSQL_NAME = os.getenv('env_db_database')
MYSQL_USER = os.getenv('env_db_user')
MYSQL_PASSWORD = os.getenv('env_db_password')
MYSQL_PORT = os.getenv('env_db_port')

DATABASES_MYSQL = {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': MYSQL_HOST,
        'NAME': MYSQL_NAME,
        'USER': MYSQL_USER,
        'PASSWORD': MYSQL_PASSWORD,
        'PORT': MYSQL_PORT,
        'CONN_MAX_AGE': 27800,
        'OPTIONS': {
            'autocommit': True,
        },
    }
