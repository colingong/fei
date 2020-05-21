from django.urls import path, include
from . import views

app_name = 'app_cache'

urlpatterns = [
    path('alive/', views.alive, name='alive'),
    path('cached/<int:product_id>/', views.cached_product, name='cached-product'),
    path('nocached/<int:product_id>/', views.not_cached_product, name='no-cached-product'),
]