"""用户订单
   UserOrder: 用户下的订单
   SubUserOrder: 如果需要，用户订单可能会分成几个；
      如果没有拆分，那么就当成一个子订单，即每个用户订单，包含至少一个子订单或多个子订单
   OrderDetail: 订单详情，包括子订单号，购买的产品，每个购买产品的数量
      根据用户订购产品种类，每个用户订单对应至少一个或多个子订单
      每个子订单对应至少一个或多个订单详情
"""

from django.db import models
from .models_product import Product, Category
from django.contrib.auth.models import User

class UserOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=50)
    total_price = models.DecimalField(max_digits=18, decimal_places=2)

class SubUserOrder(models.Model):
    userorder = models.ForeignKey(UserOrder, on_delete=models.CASCADE)
    sub_userorder_number = models.CharField(max_length=50)

class OrderDetail(models.Model):
    subuserorder = models.ForeignKey(SubUserOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quntity = models.IntegerField()
