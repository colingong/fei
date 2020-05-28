# from share.config_redis import REDIS_HOST, REDIS_PORT, REDIS_DB, REDIS_PASSWORD_ALL
from share.bloom_filter_redis import bloomfilter_flushdb_then_init, BloomFilterRedis
from app_models.models import Product
from django.shortcuts import HttpResponse

def init_bloom_filter(request, model_name):
    bloomfilter_flushdb_then_init(key=model_name)
    products = Product.objects.all()

    bf = BloomFilterRedis(key=model_name)
    for p in products:
        bf.add(p.id)
    
    print(f'---> bitcount of {bf.redis_key}: {bf.redis.bitcount(bf.redis_key)}')
        
    return HttpResponse('ok')


def bloom_filter_product(request):
    pass
