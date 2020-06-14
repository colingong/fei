from django.urls import path, include
from . import views
from . import views_account

urlpatterns = [
    path('alive/', views.alive, name='alive'),
    path('new/', views_account.create_user, name='create-user'),
]