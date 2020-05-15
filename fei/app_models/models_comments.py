"""留言功能
"""

from django.db import models

class AnonymousComments(models.Model):
    """匿名留言

        用户名，电话，email，都可以空白
    """

    username = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    comments = models.CharField(max_length=200)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username + str(self.create_time)