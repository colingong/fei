from django.shortcuts import render, HttpResponse

# Create your views here.
def alive(request):
    return HttpResponse('app_demo1/alive/')