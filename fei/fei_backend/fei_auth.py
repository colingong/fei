"""自定义一个认证的backend
"""
from django.contrib.auth.models import User
from app_models.models import UserExtra
from django.contrib.auth.hashers import check_password


class FeiAuth(object):
    """任意组合的认证方式

        可以使用 username, email, qq, phone中的任意一个作为用户名 
        密码符合 user.password，userextra.pay_password中的任意一个，即成功认证

    """
    def authenticate(self, request, username=None, password=None):
        print('========> start FeiAuth')
        in_pass = request.POST.get('password', None)
        try:
            u = User.objects.get(username=request.POST.get('username'))
            if check_password(in_pass, u.password) or check_password(in_pass, u.userextra.pay_password):
                return u
        except:
            pass

        try:
            u = User.objects.get(email=request.POST.get('username'))
            if check_password(in_pass, u.password) or check_password(in_pass, u.userextra.pay_password):
                return u
        except:
            pass

        try:
            user_extra = UserExtra.objects.get(qq=request.POST.get('username'))
            if check_password(in_pass, user_extra.pay_password) or check_password(in_pass, user_extra.user.password):
                return user_extra.user
        except:
            pass

        try:
            user_extra = UserExtra.objects.get(phone=request.POST.get('username'))
            if check_password(in_pass, user_extra.pay_password) or check_password(in_pass, user_extra.user.password):
                return user_extra.user
        except:
            pass

        return None



    def get_user(self, user_id):
        return User.objects.get(id=user_id)

class WeixinAuth(object):
    pass

class PhoneAuth(object):
    def authenticate(self, request, username=None, password=None):
        pass
    
    def get_user(self, user_id):
        pass

class QqAuth(object):
    def authenticate(self, request, username=None, password=None):
        pass

    def get_user(self, user_id):
        pass


