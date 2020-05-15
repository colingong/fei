from django.shortcuts import render, HttpResponse

# Create your views here.
def alive(request):
    return HttpResponse('alive - clientip')

def root_echoip(request):
    headers = request.headers
    print('ECHOIP --->')
    print(headers)
    return HttpResponse('ok')
