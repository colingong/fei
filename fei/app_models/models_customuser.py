from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    chinese_name = models.CharField(max_length=50, unique=True, blank=False)
    chinese_pass = models.CharField(max_length=100, blank=True)
    chinese_addr = models.CharField(max_length=200, blank=True)
    chinese_info = models.CharField(max_length=30, blank=True)