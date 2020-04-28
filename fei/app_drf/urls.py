from rest_framework import routers

from django.urls import path, include
from . import views
from . import views_drf1
from . import views_token
from . import views_customize_serializer
from . import views_apiview_to_router
from . import views_v2

app_name = 'app_drf'

# for views_v2
router_v2 = routers.DefaultRouter()
router_v2.register('user', views_v2.UserViewSet)
router_v2.register('product', views_v2.ProductViewSet)

urlpatterns = [
    # path('api-token-auth/', views_token.drf_views.obtain_auth_token, name='api-token-auth'),
]