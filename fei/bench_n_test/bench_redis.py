"""测试腾讯云上的三个redis实例

    1. 1C1G ECS上，docker 里运行的redis实例（本机）
    2. 1C1G redis实例，腾讯云上的redis实例
    3. 4C8G ECS上，docker 里运行的redis实例

    测试结果：
        # 本机
        64 bytes from 10.0.0.13: icmp_seq=1 ttl=64 time=0.051 ms
        64 bytes from 10.0.0.13: icmp_seq=2 ttl=64 time=0.047 ms
        start bench redis1
        Duration: 5.584269046783447

        # 同地址域不同区的一个redis实例
        # redis-cli --latency -h 10.0.2.4 -p 6379
        # min: 1, max: 7, avg: 1.56 (343 samples)^C
        # 这个延迟达到1.56，也是相当的高；不过和两台同子网内的延迟比起来，似乎又不算历害了
        start bench redis2金
        Duration: 52.816078186035156

        # 同区（成都一区）内同子网的另一台主机
        # 64 bytes from 10.0.0.22: icmp_seq=3 ttl=63 time=1.76 ms
        # 64 bytes from 10.0.0.22: icmp_seq=4 ttl=63 time=1.72 ms
        # 同子网内，这个延迟高的有点离谱
        start bench redis3
        Duration: 57.26516246795654

    仅从set来看，这个内网延迟很有点高；这么高的延迟，get都不用测了
    对于redis，连接池看来还是很有必要的，随便延迟高一点的话，完全发挥不出来它的优势
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