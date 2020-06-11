"""test for config_redis.py
"""
import unittest
import os, sys
from django.test import TestCase
from unittest.mock import patch

# from share.config_redis import redis_rate_limit
# try:
#     from share.config_redis import REDIS_LOCATION, REDIS_HOST, REDIS_PORT, REDIS_DB, REDIS_PASSWORD_ALL
# except:
#     pass

class TestRedisConfig(unittest.TestCase):
    def setUp(self):
        # import os
        # os.environ['env_redis_location'] = 'mysite.com'
        # os.environ['redis_host'] = '127.0.0.1'
        # os.environ['redis_port'] = '666'
        # os.environ['redis_db'] = '0'
        # os.environ['redis_password'] = 'REDISPASS'
        # os.environ['demo_env'] = '9876'
        pass

    # def test_redis_env(self):
        import os
        os.environ['env_redis_location'] = 'mysite.com'
        os.environ['redis_host'] = '127.0.0.1'
        os.environ['redis_port'] = '6379'
        os.environ['redis_db'] = '2'
        os.environ['redis_password'] = 'REDISPASS'
        os.environ['demo_env'] = '9876'
        from .config_redis import REDIS_LOCATION, REDIS_HOST, REDIS_PORT, REDIS_DB, REDIS_PASSWORD_ALL
        from .config_redis import redis_rate_limit
        print(redis_rate_limit)

    def test_redis_env2(self):
        import os
        from .env_exceptions import EnvRedisException
        # os.environ['env_redis_location'] = 'mysite.com'
        os.environ['redis_host'] = '127.0.0.1'
        os.environ['redis_port'] = '6379'
        os.environ['redis_db'] = '2'
        os.environ['redis_password'] = 'REDISPASS'
        os.environ['demo_env'] = '9876'
        
        with self.assertRaises(EnvRedisException):
            from .config_redis import REDIS_LOCATION
            pass


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
