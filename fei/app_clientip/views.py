from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
# Create your views here.
def alive(request):
    return HttpResponse('alive - clientip')

def root_echoip(request):
    d = {'Your IP': request.headers.get('X-Real-Ip', 'Not get your ip! ')}
    return JsonResponse(d)
