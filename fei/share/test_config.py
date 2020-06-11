from django.test import TestCase

class DemoTest(TestCase):
    def setUp(self):
        pass

    def test1(self):
        print("开始测试-share/test_config.py")
        self.assertEqual(1, 1, 'hahah')