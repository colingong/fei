"""检查用户是否能被drf 认证
    用户已经生成了token才可以被认证
"""
from rest_framework import authentication

def drf_user_info(get_response):
    def wrapper(request):
        result = get_response(request)
        try:
            user, token = authentication.TokenAuthentication().authenticate(request)
            print(f'--- MIDDLEWARE [drf_user_inf] : ID /User / Token] ---> {user.id} / {user} / {token}')
        except:
            print(f'--- MIDDLEWARE [drf_user_inf] AUTH FAILED!')

        return result
    return wrapper