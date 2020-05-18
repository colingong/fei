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
    weixin_openid = models.CharField(max_length=50, unique=True, null=True, blank=True)
    phone = models.CharField(max_length=11, unique=True, null=True, blank=True)
    qq = models.CharField(max_length=50, unique=True, null=True, blank=True)
    pay_password = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f'extra_user {self.user.username}'


from django.contrib.auth.hashers import make_password
class UserExtraTest(models.Model):
    """[扩展django的用户模型]
       user 是一个OneToOneField
    
    Arguments:
        models {[type]} -- [description]
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    weixin_openid = models.CharField(max_length=50, unique=True, null=True, blank=True)
    phone = models.CharField(max_length=11, unique=True, null=True, blank=True)
    qq = models.CharField(max_length=50, unique=True, null=True, blank=True)
    _pay_password = models.CharField(max_length=50, blank=True, db_column='pay_password')

    def __str__(self):
        return f'extra_user {self.user.username}'

    @property
    def pay_password(self):
        return self._pay_password

    @pay_password.setter
    def pay_password(self, raw_password):
        hashed_password = make_password(raw_password)
        self._pay_password = hashed_password


