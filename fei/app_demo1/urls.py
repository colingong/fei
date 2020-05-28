from django.urls import path
from . import views

urlpatterns = [
    path('', views.alive, name='alive'),
    path('test/', views.test, name='test'),

    path('echo_env/<str:var_name>/', views.echo_env, name='echo_env'),
    path('datetime/', views.echo_datetime, name='datetime'),
]
