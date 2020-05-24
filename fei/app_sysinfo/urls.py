from django.urls import path, include
from . import views

app_name = 'app_sysinfo'

urlpatterns = [
    path('', views.uwsgi_reload_info, name='info'),
]