from django.urls import path, include
from . import views

app_name = 'app_drf'

urlpatterns = [
    # User and UserExtra combined view
    path('feiview/<int:pk>/', views.FeiView.as_view(), name='feiview'),
]