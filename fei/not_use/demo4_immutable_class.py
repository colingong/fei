"""create a immutable object
"""

class MyImmutable(object):
    """一个immutable的类
       当这个实例初始化之后，禁用掉__setatt__和__delattr__，本实例即成为一个immutable对象
       实际上用户当然可以用其它方式来修改这个对象，但是用户会自已负责

       实际上这是一个约定，而非强烈的约束
    """
    def __init__(self, a, b):
        object.__setattr__(self, 'a', a)
        object.__setattr__(self, 'b', b)

    def __setattr__(self, *args):
        """重新赋值会抛exception"""
        raise Exception('不能set')

    def __delattr__(self, *args):
        """删除属性也会抛exception"""
        raise Exception('不能get')

import collections

my_immutable = collections.namedtuple('my_immutable', ('a', 'b'))

if __name__ == '__main__':
    # m1 = MyImmutable(3, 6)
    # print(m1.a, m1.b)
    # m1.a = 10
    # m1.b = 20
    # print(m1.a, m1.b)
    my_immutable.a = 3
    print(my_immutable)
    print(my_immutable.a)
    my_immutable.a = 4
    print(my_immutable[0])