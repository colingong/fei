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

from .models_extra_user import UserExtra