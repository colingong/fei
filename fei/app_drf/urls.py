from django.urls import path, include
from . import views
from . import views_drf1

app_name = 'app_drf'

urlpatterns = [
    # User and UserExtra combined view
    path('feiview/<int:pk>/', views.FeiView.as_view(), name='feiview'),
    path('send_json/', views.send_json, name='send_json'),

    # views_drf1
    path('show_user/<int:pk>/', views_drf1.show_user, name='show_user'),
    path('full_info/<int:pk>/', views_drf1.full_user, name='full_user'),
    # path('user_and_extra/<int:pk>/', views_drf1.user_and_extra, name='user_and_extra'),
]