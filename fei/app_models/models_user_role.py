"""用户角色模型
    简单快速的实现一个基于角色的权限控制 /rbac
    用户和用户角色，是一对多的关系
    不过现实的系统里，绝大多数用户只会具有一个角色，例如已认证用户或未认证用户
    少数用户可能具有多个角色
    这样总体来说，角色表的记录并不会膨胀到特别大，和用户表的记录数接近，略多一点，性能可以接受
    当一个用户从未认证客户，经过认证变成已认证客户，一般仅保留认证客户的角色，未认证角色将会删除，这一点由认证的逻辑保证
    在每个视图需要权限控制的视图，用装饰器来实现：
    @require_userrole()
"""

from django.db import models
from django.contrib.auth.models import User

ROLE_CHOICES = (
    ('VIP_CUSTOMER', 'VIP客户'),
    ('SYSTEM_ADMIN', '系统管理员'),
    ('BUSINESS_ADMIN', '商城管理员'),
    ('VEIRFIED_CUSTOMER', '已认证客户'),
    ('UNVERIFIED_CUSTOMER', '未认证客户'),
)
class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role_code = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f'{self.role_code} - {self.user.username}'