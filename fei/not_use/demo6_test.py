import unittest

def raise_exception(*args, **kwargs):
    raise ValueError(f'值错误 {args} / {kwargs}')
    # raise FileNotFoundError

class StartTest(unittest.TestCase):

    def test(self):
        self.assertTrue(True, '第一个测试')

    def test_pass(self):
        self.assertTrue(True, '第二个测试')

    def test_fail(self):
        self.assertFalse(False, '第三个测试')

    # def test_error(self):
    #     raise Exception('---> raise a exception')

    def test_trap_locally(self):
        try:
            raise_exception('a', b='c')
        except ValueError:
            pass
        else:
            self.fail('未捕获 ValueError')
    
    def setUp(self):
        print('---> 开始 setUp() 方法')
    
    def tearDown(self):
        print('===> tearDown')

if __name__ == '__main__':
    unittest.main()
