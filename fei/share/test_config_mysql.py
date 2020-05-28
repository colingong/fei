import unittest
from share.config_mysql import MYSQL_HOST, MYSQL_NAME, MYSQL_USER, MYSQL_PASSWORD, MYSQL_PORT

class MysqlConfigTest(unittest.TestCase):
    def test_mysql_host(self):
        self.assertIsInstance(MYSQL_HOST, str)
    def test_mysql_name(self):
        self.assertIsInstance(MYSQL_NAME, str)
    def test_mysql_user(self):
        self.assertIsInstance(MYSQL_USER, str)
    def test_mysql_password(self):
        self.assertIsInstance(MYSQL_PASSWORD, str)
    def test_mysql_port(self):
        self.assertIsInstance(MYSQL_PORT, str)

if __name__ == '__main__':
    unittest.main()
