"""test for config_redis.py
"""
import unittest
from django.test import TestCase
from share.config_redis import REDIS_LOCATION, REDIS_HOST, REDIS_PORT, REDIS_DB, REDIS_PASSWORD_ALL

class TestRedisConfig(unittest.TestCase):
    def test_redis_location(self):
        self.assertIsInstance(REDIS_LOCATION, str)

    def test_redis_host(self):
        self.assertIsInstance(REDIS_HOST, str)
        
    def test_redis_port(self):
        self.assertIsInstance(REDIS_PORT, int)
        
    def test_redis_db(self):
        self.assertIsInstance(REDIS_DB, int)
        
    def test_redis_password_all(self):
        self.assertIsInstance(REDIS_PASSWORD_ALL, str)

if __name__ == '__main__':
    unittest.main()
