"""test for config_redis.py
"""
import unittest
import os, sys
from django.test import TestCase
from unittest.mock import patch

class TestRedisConfig(unittest.TestCase):
    def setUp(self):
        # os.environ['env_redis_location'] = 'mysite.com'
        # os.environ['redis_host'] = '127.0.0.1'
        # os.environ['redis_port'] = '6379'
        # os.environ['redis_db'] = '2'
        # os.environ['redis_password'] = 'REDISPASS'
        # os.environ['demo_env'] = '9876'
        pass

    def test_redis_env_not_set(self):
        from .env_exceptions import EnvRedisException
        with self.assertRaises(EnvRedisException):
            from .config_redis import _RedisConfig
            _RedisConfig.REDIS_LOCATION = _RedisConfig.FOR_UNITTEST
            _RedisConfig.check_env_or_raise()

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
