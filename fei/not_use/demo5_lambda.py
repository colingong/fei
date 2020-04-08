"""decorator"""
from functools import wraps

def dec(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('good')
        return func(*args, **kwargs)

    return wrapper

@dec
def sum(x, y):
    return x + y

if __name__ == '__main__':
    print(sum(1, 2))
    print(sum.__name__)

