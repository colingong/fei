"""main_settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
   https://docs.djangoproject.com/en/2.2/topics/http/urls/

Examples:

Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""

from django.contrib import admin
from django.urls import path, include
from . import views

from rest_framework import routers

# from app_drf.urls import router as drf_router
# router = routers.DefaultRouter()
# router.registry.extend(drf_router.registry)

from app_drf.urls import router_v2 as drf_router_v2
router2 = routers.DefaultRouter()
router2.registry.extend(drf_router_v2.registry)

# router.register(r'users', app_drf_views.UserViewSet)
# router.register(r'userextras', app_drf_views.UserExtraViewSet)
# router.register(r'feiviewset', app_drf_views.FeiViewSet, basename='feiviewset')
# router.register(r'user_and_extra', views_apiview_to_router.UserAndExtra, basename='custome_api')

urlpatterns = [
    # path('', include(router.urls)),
    # path('api/', include(router.urls)),
    # path('api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('v2/', include(router2.urls)),
    
    
    path('admin/', admin.site.urls),
    path('demo1/', include('app_demo1.urls')),
    path('models/', include('app_models.urls')),
    # path('drf/', i', include('app_drf.urls')),
    ]

