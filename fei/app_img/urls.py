from django.urls import path, include
from . import views
from . import views_img_upload

app_name = 'app_img'

urlpatterns = [
    path('alive/', views.alive, name='alive'),

    path('upload/', views_img_upload.upload, name='upload'),
    path('pic001/', views_img_upload.display_img, name='display-img'),

    path('emoji/', views_img_upload.emoji, name='emoji'),
]