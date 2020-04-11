from django.urls import path, include
from . import views

app_name = 'app_drf'

urlpatterns = [
    # User and UserExtra combined view
    path('user_userextra/', views.UserUserExtraView, name='user-userextra'),
    # path('user_userextra/<int:pk>/', views.user_userextra, name='user-userextra'),
    path('feiview/<int:pk>/', views.FeiView.as_view(), name='feiview'),
]