from django.contrib.auth.models import User
from app_models.models import UserExtra
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'objects']

class UserExtraSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserExtra
        fields = ['url', 'weixin_openid', 'phone', 'qq', 'pay_password']
