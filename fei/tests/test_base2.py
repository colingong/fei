from django.test import TestCase
from django.test import SimpleTestCase
from django.contrib.auth.models import User

class DemoTest(TestCase):

    def setUp(self):
        u1 = User(username='abc')
        u1.save()
        u2 = User(username='def')
        u2.save()

    def test_demo(self):
        self.assertEqual('a', 'a')
        self.assertNotEqual('a', 'b')
    
    def test_demo2(self):
        self.assertListEqual([1, 2, 3], [1, 2, 3])

    def test_count_user(self):
        users = User.objects.all()
        user_count = users.count()
        
        self.assertEqual(user_count, 2)

    def test_len_user(self):
        users = User.objects.all()
        self.assertEqual(len(users), 2)

class SimpleDemo(SimpleTestCase):

    def setUp(self):
        pass

    def test_simple_1(self):
        self.assertEqual(1, 1)
        self.assertNotEqual(1, 0)
        