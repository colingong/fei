"""
"""

from rest_framework import views
from rest_framework import serializers
from rest_framework import response
from rest_framework import permissions
from share.fei_debug import block_print

class CustomSerializer(serializers.Serializer):
    userid = serializers.IntegerField()
    name = serializers.CharField(max_length=15)
    balance = serializers.DecimalField(max_digits=18, decimal_places=2)

from rest_framework.permissions import BasePermission
class EnableAllUsers(BasePermission):
    # has_permission = True
    # has_object_permission = True
    def has_permission(self, request, view):
        return True

class CustomView(views.APIView):
    # permissions = [permissions.AllowAny]
    # authentication_classes = [permissions.AllowAny]
    permission_classes = [EnableAllUsers, ]

    def get(self, request):
        """
        request的GET方法
        request  -- django 的 request 对象
        """
        data = {
            'userid': 996,
            'name': 'feifeifei',
            'balance': 123.4567}
        serializer = CustomSerializer(data)
        block_print(serializer.__dict__)
        resp = response.Response(serializer.data)
        block_print(resp)
        return response.Response(serializer.data)


    # def post(self, request, format=None):
    #     pass
