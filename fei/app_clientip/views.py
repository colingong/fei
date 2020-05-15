from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
# Create your views here.
def alive(request):
    return HttpResponse('alive - clientip')

def root_echoip(request):
    """返回访问者的ip

        有时候想知道自已的公网ip，就直接用这个好了

        先从nginx取'X-Real-Ip'）
        由于用了nginx作为反向代理，需要在nginx里如下配置，然后获取 X-Real-IP即可
            location / {
                proxy_set_header Host $host;
                proxy_set_header X-Real-Ip  $remote_addr;
                proxy_set_header X-Forwarded-For $remote_addr;
                proxy_pass http://10.0.3.115;
            }

        如果django前面没有nginx，就直接从 request.META里取 'REMOTE_ADDR'
    """
    ipaddress = request.headers.get('X-Real-Ip', request.META.get('REMOTE_ADDR'))
    d = {'Your IP': ipaddress}
    return JsonResponse(d)
