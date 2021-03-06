# -*- coding: utf-8 -*-

from app_drf.views_apiview_to_router import UserAndExtra
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from rest_framework import routers

from django.urls import path, include
from . import views
from . import views_drf1
from . import views_token
from . import views_customize_serializer
from . import views_apiview_to_router
from . import views_v2
from . import views_v3
from . import views_perm_any

app_name = 'app_drf'

# for views_v2
router_v2 = routers.DefaultRouter()
router_v2.register('user', views_v2.UserViewSet)
router_v2.register('product', views_v2.ProductViewSet)
router_v2.register('category', views_v2.CategoryViewSet)
router_v2.register('userorder', views_v2.UserOrderViewSet)
router_v2.register('warehouse', views_v2.WarehouseViewSet)
router_v2.register('supplier', views_v2.SupplierViewSet)
router_v2.register('fulluser', views_v2.FulluserViewSet)
# router_v2.register('register', views_perm_any.UserRegisterViewSet)
router_v2.register('new/product', views_perm_any.NewProductViewSet)

urlpatterns = [
    path('my_token/', views_token.drf_views.obtain_auth_token, name='my_token'),
    # APIViews
    path('view1/', views_v3.CustomView.as_view(), name='view1'),
    path('view2/', views_v3.view2, name='view2'),

    # any user have permission
    path('any/', views_v3.CustomView.as_view(), name='any'), 

    # demo ofor schema
    path('openapi/', get_schema_view(
        title="Fei - 使用 Django & Django Rest Framewrok 开发",
        description="本项目openapi",
        version="0.0.1",
    ), name='openapi-schema'),

    # swagger
    path('swagger/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'app_drf:openapi-schema'},
        ), name='swagger'),
    ]
