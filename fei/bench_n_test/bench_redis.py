"""测试腾讯云上的三个redis实例

    1. 1C1G ECS上，docker 里运行的redis实例（本机）
    2. 1C1G redis实例，腾讯云上的redis实例
    3. 4C8G ECS上，docker 里运行的redis实例
"""
import os, sys
import time

PROJECT_ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main_settings.settings")
import django
django.setup()

import redis
from share.config_redis import REDIS_PASSWORD_ALL

# 1. 1C1G ECS上，docker 里运行的redis实例（本机） 
# redis1 = redis.Redis(url=f'rediss://:{REDIS_PASSWORD_ALL}@10.0.0.13:6397/3')
redis1 = redis.Redis(
    host='10.0.0.13',
    port=6379,
    db=3,
    password=REDIS_PASSWORD_ALL)

# 2. 1C1G redis实例，腾讯云上的redis实例
# redis2 = redis.Redis(url=f'rediss://:{REDIS_PASSWORD_ALL}@10.0.2.4:6397/3')
redis2 = redis.Redis(
    host='10.0.2.4',
    port=6379,
    db=3,
    password=REDIS_PASSWORD_ALL)

# 3. 4C8G ECS上，docker 里运行的redis实例
# redis3 = redis.Redis(url=f'rediss://:{REDIS_PASSWORD_ALL}@10.0.0.22:6397/3')
redis3 = redis.Redis(
    host='10.0.0.22',
    port=6379,
    db=3,
    password=REDIS_PASSWORD_ALL)

def bench_redis(redis_conf, repeat_count):
    start = float(time.time())
    r = redis_conf
    for i in range(repeat_count):
        r.set(str(i), str(i))
    end = float(time.time())
    print(f'Duration: {end - start}')

if __name__ == '__main__':
    print('start bench redis1')
    bench_redis(redis1, 30000)
    print('start bench redis2')
    bench_redis(redis2, 30000)
    print('start bench redis3')
    bench_redis(redis3, 30000)
    print('--- done ---')