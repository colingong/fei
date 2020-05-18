"""自定义一个认证的backend
"""

class EmailAuth(object):
    auth_fields = ('user.email', 'user.userextra.qq', 'user.userextra.phone')
    auth_passwords = ('user.password', 'user.userextra.pay_password')
    def authenticate(self, request, username=None, password=None):
        input_user = request.POST.get('username')
        input_password = request.POST.get('password', None)
        

    def get_user(self, user_id):
        pass

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


