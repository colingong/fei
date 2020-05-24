from django.db import models

class SiteLog(models.Model):
    """日志记录

    Arguments:
        models {[type]} -- [description]
    """
    ip = models.GenericIPAddressField(null=True)
    userid = models.IntegerField()
    username = models.CharField(max_length=50)
    datetime = models.DateTimeField(auto_now_add=True)
    url = models.URLField(max_length=250)
    method = models.CharField(max_length=15)
    payload = models.CharField(max_length=1024)

    def __str__(self):
        return f'LOG_{self.username}'