# from fei_contextprocessors.page_header import context_header
# from fei_contextprocessors.page_header import context_header
import os
from django.shortcuts import render, HttpResponse
import time
import random

# Create your views here.
def alive(request):
    return HttpResponse('app_demo1/alive/')

def test(request):
    return HttpResponse('/demo1/test/')


def echo_env(request, var_name):
    # os_env_var = os.getenv(var_name, f'no var named: {var_name}')
    # return HttpResponse(os_env_var)
    return HttpResponse('<h2>功能被禁止！</h2>')

def echo_datetime(request):
    x = random.random()
    time.sleep(3)
    current = time.strftime('%m-%d %H:%M:%S')
    return HttpResponse(f'{current} <br>"\n" ')

def context_demo(request):
    return render(request, 'app_demo1/test_context_processer.html')

from .tasks import celery_task_console_log_num
def celery_jobs(request):
    for i in range(3):
        celery_task_console_log_num.delay(i)
    return HttpResponse('celery jobs run')
