from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.core.cache import cache

# Create your views here.
def alive(request):
    return HttpResponse('app_cache, alive\n')

from app_models.models import Product

def cached_product(request, product_id):
    p = cache.get(f'product_{product_id}')
    if p:
        return JsonResponse({"Cache": "---> HIT", "object": p}, safe=False)
    else:
        p = list(Product.objects.filter(id=product_id).values())
        cache.set(f'product_{product_id}', p, 987)
        return JsonResponse({"Cache": "===XXX MISSED", "object": p}, safe=False)

def not_cached_product(request, product_id):
    p = list(Product.objects.filter(id=product_id).values())
    return JsonResponse({"NoCache": " No Cache!", "object": p}, safe=False)

def clear_cache(request):
    cache.clear()
    return HttpResponse('ok')