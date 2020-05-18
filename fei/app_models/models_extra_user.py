"""[使用one to one扩展User模型]
"""
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserExtra(models.Model):
    """[扩展django的用户模型]
       user 是一个OneToOneField
    
    Arguments:
        models {[type]} -- [description]
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    weixin_openid = models.CharField(max_length=50, unique=True, null=True, blank=True)
    phone = models.CharField(max_length=11, unique=True, null=True, blank=True)
    qq = models.CharField(max_length=50, unique=True, null=True, blank=True)
    pay_password = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'extra_user {self.user.username}'

    def save(self, *args, **kwargs):
        self.pay_password = make_password(self.pay_password)
        super().save()
