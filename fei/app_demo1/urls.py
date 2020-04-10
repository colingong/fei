from django.urls import path
from . import views

urlpatterns = [
    path('', views.alive, name='alive'),
    path('test/', views.test, name='test'),
]
