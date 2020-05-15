from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
# Create your views here.
def alive(request):
    return HttpResponse('alive - clientip')

def root_echoip(request):
    request_headers = request.headers
    print('ECHOIP --->')
    print(request_headers)
    echo_headers = ['X-Real-Ip', 'X-Forwarded-For']
    d = {k: v for k, v in request.headers.items() if k in echo_headers}
    return JsonResponse(d)
