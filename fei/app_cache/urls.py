from django.urls import path, include
from . import views
from . import views_bloom_filter

app_name = 'app_cache'

urlpatterns = [
    path('alive/', views.alive, name='alive'),
    path('cached/<int:product_id>/', views.cached_product, name='cached-product'),
    path('nocached/<int:product_id>/', views.not_cached_product, name='no-cached-product'),
    path('clear/', views.clear_cache, name='clear'),
    path('bf/init/<str:model_name>/', views_bloom_filter.init_bloom_filter, name='init-bloom-filter'),
]