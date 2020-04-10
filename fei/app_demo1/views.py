from django.shortcuts import render, HttpResponse

# Create your views here.
def alive(request):
    return HttpResponse('app_demo1/alive/')

def test(request):
    return HttpResponse('/demo1/test/')