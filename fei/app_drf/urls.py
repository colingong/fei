from rest_framework import routers

from django.urls import path, include
from . import views
from . import views_drf1
from . import views_token
from . import views_customize_serializer
from . import views_apiview_to_router
from . import views_v2

app_name = 'app_drf'

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('userextra', views.UserExtraViewSet)
# router.register('feiviewset', views.FeiViewSet, basename='feiviewset')
# router.register('user_and_extra', views_apiview_to_router.UserAndExtra, basename='custom_api')

# for views_v2
router_v2 = routers.DefaultRouter()
router_v2.register('user', views_v2.UserViewSet)
router_v2.register('product', views_v2.ProductViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # # User and UserExtra combined view
    # path('feiview/<int:pk>/', views.FeiView.as_view(), name='feiview'),
    path('send_json/', views.send_json, name='send_json'),

    # # views_drf1
    # path('show_user/<int:pk>/', views_drf1.show_user, name='show_user'),
    # path('full_info/<int:pk>/', views_drf1.full_user, name='full_user'),
    # # path('user_and_extra/<int:pk>/', views_drf1.user_and_extra, name='user_and_extra'),

    # # token demo
    # path('api-token-auth/', views_token.drf_views.obtain_auth_token, name='api-token-auth'),

    # # views_customize_serializer
    # path('user_all_info/<int:pk>/', views_customize_serializer.show_user_all_info, name='user-all-info'),

]