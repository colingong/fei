from django.urls import path, include
from . import views 

app_name = 'app_comments'

urlpatterns = [
    path('leave_comments/', views.leave_comments, name='leave-comments'),
]