from django.urls import path, include
from . import views
from . import views_img_upload

app_name = 'app_img'

urlpatterns = [
    path('alive/', views.alive, name='alive'),

    # 生成带文字的emoji图片
    path('emoji/', views_img_upload.emoji, name='emoji'),
]