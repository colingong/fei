"""[项目的models]
   所有models的定义都在同目录下其它的文件中定义
   所有定义models的文件，命名都类似这样：models_for_some_app.py
   所有app用到的models都从这里import
   from .models_for_some_app import MyModel
"""
from django.db import models
# Create your models here.

# A custom user model, extended from Abstractuser
# Just use django default User model
# from .models_customuser import CustomUser
# CustomerUser NOT used , just a practice

# from django.contrib.auth.models import User
from .models_extra_user import UserExtra
from .models_product import Warehouse, Category,  Product, Supplier
from .models_order import UserOrder, SubUserOrder, OrderDetail
from .models_user_role import UserRole
from .models_user_asset import UserAsset
from .models_comments import AnonymousComments
from .models_log import UserLog, SysLog
from django.contrib.auth.models import User

# for drf authentication
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# 测试 user_instance.token attribute error的问题
# from .models_drf_token import ProxyToken

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
   if created:
      Token.objects.create(user=instance)
