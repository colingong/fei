"""views just for drf"""

from django.contrib.auth.models import User
from app_models.models import UserExtra
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

        
class UserSerializer(serializers.ModelSerializer):
    api_desc = serializers.SerializerMethodField('comment_for_user')

    def comment_for_user(self, pk=None):
        return 'API接口说明： 这是一个用户信息列表'

    class Meta:
        model = User
        # fields = '__all__'
        fields = ['api_desc', 'username', 'first_name', 'last_name', 'is_active']

# @api_view()
# def show_user(request, pk):
#     user = User.objects.get(id=pk)
#     user_serializer = UserSerializer(user)
#     print(type(user_serializer.data))
#     for k, v in user_serializer.data.items():
#         print(f'{k} ===> {v}')
#     print(f'---> {user_serializer.data}')
#     return Response({'user': user_serializer.data})

@api_view()
def show_user(request, pk):
    # custom_data = {"key1": "value1", "key2": "value2", "username": "custom_data_username"}
    
    user_serializer = UserSerializer(request.user)

    return Response({'user': user_serializer.data})

# 把两个one to one的表，组合到同一个view中
# 这里有可能不合适的地方是，extra_info会成为user的一个嵌套的子集
class UserExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserExtra
        fields = '__all__'

class FullUserSerializer(serializers.ModelSerializer):
    extra_info = UserExtraSerializer()
    class Meta:
        model = User
        fields = '__all__'

@api_view()
def full_user(request, pk):
    extra_info = UserExtra.objects.get(id=pk)
    user = User.objects.get(id=pk)
    user.extra_info = extra_info
    full_info_serializer = FullUserSerializer(instance=user)
    # full_info_serializer.is_valid()

    return Response({'user': full_info_serializer.data})

# 把两个one to one的表，组合到一个view中
# 这种方法，两个组合起来的表，看起来好象就是同一个表一样
class UserAndExtraSerializer(serializers.Serializer):
    username = serializers.CharField()
    first_name = serializers.CharField()
    weixin_openid = serializers.CharField()
    qq = serializers.CharField()

@api_view()
def user_and_extra(request, pk):
    user = User.objects.get(id=pk)
    print(user.userextra)
    user_and_extra = {'username': user.username,
        'first_name': user.first_name,
        'weixin_openid': user.userextra.weixin_openid,
        'qq': user.userextra.qq}
    user_and_extra_ser = UserAndExtraSerializer(data=user_and_extra)
    user_and_extra_ser.is_valid()
    return Response({'user and extra info': user_and_extra_ser.data})
