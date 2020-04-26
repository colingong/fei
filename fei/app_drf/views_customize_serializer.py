"""定制Serializer
"""

from rest_framework import serializers, response
from django.contrib.auth.models import User
from app_models.models import UserExtra, UserAsset
from rest_framework.decorators import api_view

class UserAllInfoSerializer(serializers.ModelSerializer):
    api_desc = serializers.SerializerMethodField('api_comment')
    phone = serializers.SerializerMethodField('user_phone')
    qq = serializers.SerializerMethodField('user_qq')
    balance = serializers.SerializerMethodField('user_balance')

    def user_phone(self, pk):
        user_extra = UserExtra.objects.get(user_id=pk)
        return user_extra.phone

    def user_qq(self, pk):
        user_extra = UserExtra.objects.get(user_id=pk)
        return user_extra.qq

    def user_balance(self, pk):
        # balance = UserAsset.objects.filter(user_id=pk).values_list('balance', flat=True)[0]
        user_asset = UserAsset.objects.get(user_id=pk)
        balance = user_asset.balance
        return balance


    def api_comment(self, pk=None):
        return '这是一个用户完整信息列表，包括了UserExtra，以及 UserAsset的信息'

    class Meta:
        model = User
        fields = ['api_desc', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser', 'balance', 'phone', 'qq']

@api_view()
def show_user_all_info(request, pk=None):
    user = User.objects.get(id=pk)
    user_all_info_serializer = UserAllInfoSerializer(user)
    return response.Response({'user':user_all_info_serializer.data})
