"""Print tool
"""
import time

def block_print(*args, **kwargs):
    now = str(int(time.time()))[-4:]
    print(f'\n---------- START {now} ----------')
    print(*args, **kwargs)
    print(f'==========  END  {now} ==========\n')
    

if __name__ == '__main__':
    block_print('abc')