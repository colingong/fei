"""some global views"""

from django.shortcuts import HttpResponse, Http404, render


def favicon(request):
    try:
        with open('static/favicon.ico', 'rb') as f:
            return HttpResponse(f.read(), content_type="image/x-icon")
    except:
        return Http404

def v2_root(request):
    urls = [
        '/v2/api1/',
        '/v2/api2/',
    ]
    return render(request, 'v2_apis.html', {'urls': urls})
