import os
from django.shortcuts import render, HttpResponse

# Create your views here.
def alive(request):
    return HttpResponse('app_demo1/alive/')

def test(request):
    return HttpResponse('/demo1/test/')


def echo_env(request, var_name):
    redis2 = os.getenv(var_name, f'no var named: {var_name}')
    return HttpResponse(redis2)
