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

from main_settings.views import v2_root
from django.contrib import admin
from django.urls import path, include
from . import views

from rest_framework import routers
from app_drf.urls import router_v2 as drf_router_v2

router2 = routers.DefaultRouter()
router2.registry.extend(drf_router_v2.registry)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('v2/', include(router2.urls)),
    # path('v2/', views.v2_root, name='v2'),
    # path('v2/api1/', include(router2.urls)),
    # path('v2/api2/', include('app_drf.urls')),
    
    path('admin/', admin.site.urls),
    path('demo1/', include('app_demo1.urls')),
    path('models/', include('app_models.urls')),
    path('img/', include('app_img.urls')),
    path('drf/', include('app_drf.urls')),

    path('ip/', include('app_clientip.urls')),
    path('comments/', include('app_comments.urls')),

    path('favicon.ico', views.favicon, name='favicon'),
    path('', views.site_root, name='site-root'),

    path('cache/', include('app_cache.urls')),
    path('sysinfo/', include('app_sysinfo.urls')),
    path('account/', include('app_account.urls')),
    ]
