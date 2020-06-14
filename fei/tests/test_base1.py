"""一些基础测试
"""
from django.test import TestCase
# from unittest import TestCase

class ModelTest(TestCase):

    def test_dummy(self):
        self.assertEqual(1, 1)
