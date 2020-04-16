"""用户资产表
   继续使用OneToOneField，从User模型扩展"""

from django.db import models
from django.contrib.auth.models import User

class UserAsset(models.Model):
   user = models.OneToOneField(User, on_delete=models.PROTECT)
   balance = models.DecimalField(max_digits=18, decimal_places=2)
   last_update = models.DateTimeField(auto_now=True)

   def _str__(self):
      return f'{self.user.username} asset'
      