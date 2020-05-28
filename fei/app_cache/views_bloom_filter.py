# from share.config_redis import REDIS_HOST, REDIS_PORT, REDIS_DB, REDIS_PASSWORD_ALL
from share.bloom_filter_redis import bloomfilter_flushdb_then_init
from share.bloom_filter_redis import BloomFilterRedis
from share.bloom_filter_redis import list_bloom_filter
from app_models.models import Product
from django.shortcuts import HttpResponse
from django.apps import apps

def init_bloom_filter(request, model_name):
    try:
        model = apps.get_model('app_models', model_name)
    except:
        return HttpResponse('不支持的模型操作，或者模型名称错误！')
        
    bloomfilter_flushdb_then_init(key=model_name)
    all_instance = model.objects.all()

    bf = BloomFilterRedis(key=model_name)
    for instance in all_instance:
        bf.add(instance.id)
    
    print(f'---> bitcount of {bf.redis_key}: {bf.redis.bitcount(bf.redis_key)}')
        
    return HttpResponse('ok')

def list_bf(request):
    keys = list_bloom_filter()
    flags = [e for e in keys if e.decode('utf-8').startswith('flag_')]
    for f in flags:
        keys.remove(f)
    return HttpResponse(keys)

def bloom_filter_product(request):
    pass
