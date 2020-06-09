"""漏桶算法简单实现限流
"""
from queue import Empty
from django.http import HttpResponse
from share.ratelimit_counter import redis_rate_limit, KEY, RATE_LIMIT
import time

def ratelimit(get_response):
    def wrapper(request):
        # before
        check = redis_rate_limit.rpop(KEY)
        print(f'==============> check is :{check}')
        if check is None:
        # rate_limit_queue.put('abc')
        # except:
            return HttpResponse('Busy, try later!"\n" ')
        
        result = get_response(request)
        redis_rate_limit.lpush(KEY, 1)
        return result
    return wrapper