import redis
import sys, os
try:
    from .config_redis import REDIS_PORT, REDIS_PASSWORD_ALL, REDIS_DB, REDIS_HOST    
except:
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from config_redis import REDIS_PORT, REDIS_PASSWORD_ALL, REDIS_DB, REDIS_HOST    

from hashlib import sha1
import datetime

redis_conn = redis.Redis(
    host=REDIS_HOST,
    db=4,
    port=REDIS_PORT,
    password=REDIS_PASSWORD_ALL
)

BLOOM_FILTER_SIZE = 2000000
BLOOM_FILTER_KEY = 'bfilter'

def bloomfilter_flushdb_then_init(redis=redis_conn, bit_length=BLOOM_FILTER_SIZE, key=BLOOM_FILTER_KEY):
    try:
        key = 'bloom_filter_' + key
        flag = 'flag_' + key
        current_datetime = datetime.datetime.now()
        redis.delete(key, flag)
        redis.setrange(key, bit_length, 0)
        redis.set(flag, f'current bloom filter created at {current_datetime}, and size / key: {bit_length} / {key}')
        return True
    except:
        print('Bloom Filter init failed!')
        return False

def list_bloom_filter(redis_conn=redis_conn):
    redis = redis_conn
    return redis.keys(pattern="*")

class BloomFilterRedis(object):
    def __init__(self, redis=redis_conn, bit_length=BLOOM_FILTER_SIZE, hash_count=5, key=BLOOM_FILTER_KEY):
        self.redis_key = 'bloom_filter_' + key
        self.redis = redis
        self.bit_length = bit_length
        self.hash_count = hash_count

    def add(self, item):
        for i in range(self.hash_count):
            index = self._get_index(item, i)
            self.redis.setbit(self.redis_key, index, 1)

    def _get_index(self, item, current_hash_count):
        sign = int(sha1((str(item) + str(current_hash_count)).encode('utf-8')).hexdigest(), 16)
        index = sign % self.bit_length
        return index

    def if_exist(self, item):
        for i in range(self.hash_count):
            index = self._get_index(item, i)
            if self.redis.getbit(self.redis_key, index) == 0:
                return False
        return True


if __name__ == '__main__':
    try:
        if sys.argv[1] == 'init_bloomfilter':
            key = sys.argv[2]
            print('start init bloomfilter')
            bloomfilter_flushdb_then_init(bit_length=BLOOM_FILTER_SIZE, key=key)
    except IndexError as e:
        pass

    bloom_filter = BloomFilterRedis(key='product')
    for i in range(3):
        bloom_filter.add(i)


    print(bloom_filter.if_exist(11))
    print(bloom_filter.if_exist(2))
