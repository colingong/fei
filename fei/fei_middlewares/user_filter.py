"""禁示测试用户改密码
"""
from django.shortcuts import HttpResponse

def disable_user_change_pass(get_response):
    """简单粗暴的禁止测试用户改密码

        用户更改密码的url是 /admin/password_change/
        因此判断当用户名是 'user'，并且 url里包含 admin/password_change时，判断用户修改密码
        直接返回一个警告消息即可
        一种简单的实现，但是不保证用户不能真正找到其它修改密码的办法
        生产系统不能依靠这种方式
    """
    def wrapper(request):
        if request.user.username == 'user' and 'admin/password_change' in request.path:
                print(f'-- disable_user_change_pass --'.ljust(30))
                print(f'测试用户试图修改密码!')
                return HttpResponse('<h2>测试用户不允许修改密码！</h2>')
        result = get_response(request)
        return result
    return wrapper