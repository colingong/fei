"""为当前系统中已有的用户创建token

    仅作为一个middleware的示例
    实际上为已有用户创建token可以直接在django shell里进行一次操作
    
.. code-block:
    users = User.objects.all()
    for user in users:
        if getattr(user, 'auth_token', True):
            token = Token(user=user)
            token.save()

"""

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

def generate_token_if_not_exist(get_response):
    """为用户生成一个token

        用户token在app_models/models.py里已经有一个生成功能，为每个新注册的用户生成token
        不过对于系统中已有的用户，就不起作用
        此middleware在每个用户访问的时候，会检查该用户是否已经有token，没有的话即为用户生成并入库
        
    """
    def middleware(request):
        if request.user.is_authenticated:
            try:
                request.user.auth_token
                print(f'--- MIDDLEWARE [generate_token_if_not_exist] ===> token already existed: {request.user}')

            # 对应： from django.core.exceptions import ObjectDoesNotExist
            # except ObjectDoesNotExist as e:

            # 对应： from django.contrib.auth.models import User
            except User.auth_token.RelatedObjectDoesNotExist as e:

            # 对应： from rest_framework.authtoken.models import Token
            # except Token.DoesNotExist as e:

                token = Token(user=request.user)
                token.save()

                print(f'--- MIDDLEWARE [generate_token_if_not_exist] ---> created token for user: {request.user}')
                # print(traceback.format_exc())
        response = get_response(request)
        return response
    return middleware