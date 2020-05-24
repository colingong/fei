from django.db import models

class UserLog(models.Model):
    """日志记录

    用户日志
    """
    ip = models.GenericIPAddressField(null=True)
    userid = models.IntegerField()
    username = models.CharField(max_length=50)
    datetime = models.DateTimeField(auto_now_add=True)
    url = models.URLField(max_length=250)
    method = models.CharField(max_length=15)
    payload = models.CharField(max_length=1024)

    def __str__(self):
        return f'UserLog_{self.username}'

class SysLog(models.Model):
    """系统日志

    记录系统事件
    """
    datetime = models.DateTimeField(auto_now_add=True)
    event = models.CharField(max_length=250)

    def __str__(self):
        return f'SysLog_' + str(self.datetime)
        