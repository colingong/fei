"""[使用one to one扩展User模型]
"""
from django.db import models
from django.contrib.auth.models import User

class UserExtra(models.Model):
    """[扩展django的用户模型]
       user 是一个OneToOneField
    
    Arguments:
        models {[type]} -- [description]
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    weixin_openid = models.CharField(max_length=50, unique=True, null=True)
    phone = models.CharField(max_length=11, unique=True, null=True)
    qq = models.CharField(max_length=50, unique=True, null=True)
    pay_password = models.CharField(max_length=50, blank=True)