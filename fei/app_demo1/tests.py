"""test docs"""

from django.test import TestCase

# Create your tests here.

# def demo_test():
#     """demo_test()

#     这里是自已随便写的东西
#     """
#     a = 13
#     b = 14
#     return a + b
# var = 'dalfjdals;fjldsafjldasjfldsa;fjldsajfldsaj dklasjf dsalj lda;sfj askl;j  kldsafjd'

# class T1(TestCase):
#     @staticmethod
#     def demo_test():
#         """demo_test(v='kkkkk')
#         这里是自已随便写的东西
#         """
#         print(f'app_demo1--->tests.py')
#         return True

#     @staticmethod
#     def req():
#         from django.test import Client
#         c = Client()
#         r = c.get('/demo1/')
#         print(r)
from django.test import Client

class MyTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_demo1(self):
        r = self.client.get('/demo1/')
        self.assertEqual(r.status_code, 200)
        # self.assertEqual(r.content, b'xyz')