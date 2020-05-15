from app_img.urls import urlpatterns
from django.urls import path, include
from . import views

app_name = 'app_clientip'

urlpatterns = [
    path('alive/', views.alive, name='alive'),
    path('', views.root_echoip, name='echoip'),
]