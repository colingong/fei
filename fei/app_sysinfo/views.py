from django.shortcuts import render, HttpResponse
from django.conf import settings
import os
import time

# Create your views here.
def uwsgi_reload_info(request):
    file = os.path.join(settings.BASE_DIR, 'reload_for_uwsgi')
    # get file modify time
    mtime = os.path.getmtime(file)
    with open(file, 'r' ) as f:
        lines = f.readlines()
        print(lines)
    return HttpResponse(str(lines[-1]) + '/' + str(time.ctime(mtime)))
