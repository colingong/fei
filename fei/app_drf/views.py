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

class FeiUserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'objects']

class FeiUserExtraSerializer(serializers.Serializer):
    class Meta:
        model = UserExtra
        fields = ['weixin_openid', 'qq']

class FeiView(rest_views.APIView):
    """成功显示了两个models， User , UserExtra
    """

    def get(self, request, pk, format=None, **kwargs):
        user = User.objects.get(id=pk)
        user_serializer = FeiUserSerializer(user)
        userextra = UserExtra.objects.get(id=pk)
        userextra_serializer = FeiUserExtraSerializer(userextra)
        print(f'===> {user.__dict__} / {userextra.__dict__}')
        print(f'---> {user_serializer.data} / {userextra_serializer.data}')
        return Response({
            'user': user_serializer.data,
            'userextra': userextra_serializer.data})



#############
class UserUserExtraViewSerializer(serializers.Serializer):
    user = UserSerializer()
    userextra = UserExtraSerializer()


class UserUserExtraView(rest_views.APIView):

    def get(self, request, pk):
        u = User.objects.get(id=pk)
        ue = UserExtra.objects.get(id=pk)
        u_serializer = UserSerializer(u)
        ue_serializer = UserExtraSerializer(ue)
        # u_serializer = UserSerializer(u, context={'request': request})
        # ue_serializer = UserExtraSerializer(ue, context={'request': request})
        serializer = UserUserExtraViewSerializer(data={
            'user': u_serializer.data,
            'userextra': ue_serializer.data
        })
        if serializer.is_valid():
            return Response(serializer.validated_data)


# def user_userextra(request, pk):
#     u = User.objects.get(id=pk)
#     ue = UserExtra.objects.get(id=pk)
#     # u_serializer = UserSerializer(data=u)
#     # ue_serializer = UserExtraSerializer(data=ue)
#     u_serializer = UserSerializer(u, context={'request': request})
#     ue_serializer = UserExtraSerializer(ue, context={'request': request})
#     serializer = UserUserExtraViewSerializer(data={
#         'user': u_serializer.data,
#         'userextra': ue_serializer.data
#     })
#     # return Response(serializers.validated_data)
#     if serializer.is_valid():
#         return Response(serializer.validated_data)
#         # return Response(serializers.data)
#     # else:
#     #     # return Response(serializers.validated_data)
#     #     return HttpResponse('ok')