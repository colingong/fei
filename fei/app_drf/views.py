from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from app_models.models import UserExtra
from .serializers import UserSerializer, UserExtraSerializer
from rest_framework import viewsets
from rest_framework import views as rest_views
from rest_framework.response import Response

# Create your views here.
def alive(request):
    return HttpResponse('---> /app_drf/alive/')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class UserExtraViewSet(viewsets.ModelViewSet):
    queryset = UserExtra.objects.all().order_by('id')
    serializer_class = UserExtraSerializer

from rest_framework import serializers


### 上面的的因为是 DRF的ViewSet，所以可以用router注册
### 以下因为是APIView，需要在本地的urls中，用FeiView.as_view()来显示响应，不能用router注册

class FeiUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'objects']

class FeiUserExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserExtra
        fields = ['weixin_openid', 'qq']

class FeiView(rest_views.APIView):
    """成功显示了两个models， User , UserExtra
    """

    def get(self, request, pk, format=None, **kwargs):
        user = User.objects.get(id=pk)
        user_serializer = FeiUserSerializer(instance=user)
        userextra = UserExtra.objects.get(id=pk)
        userextra_serializer = FeiUserExtraSerializer(instance=userextra)
        print(f'===> {user.__dict__} / {userextra.__dict__}')
        print(f'---> {user_serializer.data} / {userextra_serializer.data}')
        print(f'--- {user_serializer.__dict__}')
        
        return Response({
            'user': user_serializer.data,
            'userextra': userextra_serializer.data})

from rest_framework.decorators import api_view

@api_view()
def send_json(request):
    return Response({"key1": "value1"})

# Use ViewSet instead of APIView (FeiView)
class FeiViewSet(viewsets.ViewSet):
    def list(self, request, format=None, **kwargs):
        user = User.objects.all().order_by('id')
        userextra = UserExtra.objects.order_by('id')

        user_serializer = FeiUserSerializer(user, many=True)
        userextra_serializer = FeiUserExtraSerializer(userextra, many=True)
        return Response({
            'user': user_serializer.data,
            'userextra': userextra_serializer.data
        })
