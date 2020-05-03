"""V2
"""
from typing import Any
from django.contrib.auth.models import User
from app_models.models import UserExtra, UserAsset
from app_models.models import Category, Product, UserOrder, Warehouse, Supplier

from rest_framework import serializers
from rest_framework import viewsets

# User serializer and ModelViewSet
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'first_name', 'last_name']

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

# Product serializer and ModelViewSet
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# UserOrder
class UserOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserOrder
        fields = '__all__'

class UserOrderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserOrder.objects.all()
    serializer_class = UserOrderSerializer

#    Warehouse
class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'

class WarehouseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

# Supplier
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class SupplierViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

# UserExtra, UserAsset
# 这两个one-to-one的信息，和User一起显示出来
from django.core.exceptions import ObjectDoesNotExist
class FullUserSerializer(serializers.ModelSerializer):
    """显示用户的完整信息 User & UserExtra & UserAsset

    Arguments:
        weixin_openid: UserExtra / weixin_openid
        phone: UserExtra / phone
        qq: UserExtra / qq
        balance: UserAsset / balance 
    """
    weixin_openid = serializers.SerializerMethodField('get_userextra_weixin_openid')
    phone = serializers.SerializerMethodField('get_userextra_phone')
    qq = serializers.SerializerMethodField('get_userextra_qq')
    balance = serializers.SerializerMethodField('get_userasset_balance')

    def get_userextra_weixin_openid(self, instance):
        user = instance
        try:
            return user.userextra.weixin_openid
        except ObjectDoesNotExist as e:
            return '微信还没有登录过哦 😀'

    def get_userextra_phone(self, instance):
        user = instance
        try:
            return user.userextra.phone
        except ObjectDoesNotExist as e:
            return '电话号码还没有填哦 😀'
        
    def get_userextra_qq(self, instance):
        user = instance
        try:
            return user.userextra.qq
        except ObjectDoesNotExist as e:
            return 'qq号还没有填哦 😀'

    def get_userasset_balance(self, instance):
        user = instance
        try:
            return user.userasset.balance
        except ObjectDoesNotExist as e:
            return '还没有用户资产，需要登录一次才会有哦 😀'

    class Meta:
        model = User
        # fields = '__all__'
        exclude = ['password', ]

class FullUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = FullUserSerializer
#   UserExtra, UserAsset

