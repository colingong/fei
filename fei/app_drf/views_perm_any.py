"""不需要权限的apis

    例如product模型的get，未注册用户也需要有list
    注册用户的权限
"""
from rest_framework import serializers
from rest_framework import viewsets

from django.contrib.auth.models import User
from django.shortcuts import HttpResponse
from app_models.models import Product

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'email']

class UserRegisterViewSet(viewsets.ModelViewSet):
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()
    def create(self, request, format=None):
        serialized = UserRegisterSerializer(data=request.POST)
        if serialized.is_valid():
            user_password = serialized.validated_data.get('password', '')
            user = User(**serialized.validated_data)
            user.set_password(user_password)
            print(user.__dict__)
            user.save()
            return HttpResponse('')
        else:
            return HttpResponse(f'{serialized.errors}')

class NewProductSerializer(serializers.ModelSerializer):
    """Product

    fields:
        [category, warehouse, product_name, product_description, product_price, product_stock, for_sale,]
    """
    class Meta:
        model = Product
        fields = ["category", "warehouse", "product_name", "product_description", "product_price", "product_stock",]

class NewProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by("-id")
    serializer_class = NewProductSerializer
    def create(self, request, format=None):
        serialized = NewProductSerializer(data=request.POST)
        if serialized.is_valid():
            new_product = Product(**serialized.validated_data)
            new_product.save()
            return HttpResponse('success')
        return HttpResponse(serialized.errors)