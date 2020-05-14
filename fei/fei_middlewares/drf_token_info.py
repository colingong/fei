"""检查用户是已经生成了token，drf需要token才能认证用户
"""
from rest_framework import authentication

def drf_user_info(get_response):
    """log用户的id和token

        如果用户认证成功，打印出用户id和token；否则显示failed信息
        如果从浏览器访问，即使是已登录用户也会失败，因为浏览器用户是通过session认证的

        客户端直接访问的用户提供了 'Authorization: Token 954... ' 这个header才能被drf认证
        可以用curl/postman等直接模拟一个客户端的访问：
        curl -X GET -H 'Authorization: Token <此处是一个有效的token>' http://demo.hhxx.me/v2/
    """
    def wrapper(request):
        result = get_response(request)
        try:
            user, token = authentication.TokenAuthentication().authenticate(request)
            print(f'--- MIDDLEWARE [drf_user_info] : ID /User / Token] ---> {user.id} / {user} / {token}')
        except:
            print(f'--- MIDDLEWARE [drf_user_info] AUTH FAILED!')

        return result
    return wrapper