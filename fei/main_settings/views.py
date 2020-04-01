"""some global views"""

from django.shortcuts import HttpResponse, Http404
def favicon(request):
    try:
        with open('static/favicon.ico', 'rb') as f:
            return HttpResponse(f.read(), content_type="image/x-icon")
    except:
        return Http404
