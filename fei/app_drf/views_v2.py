"""V2
"""
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

