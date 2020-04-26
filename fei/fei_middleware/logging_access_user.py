"""记录当前访问的用户
"""
from django.conf import settings

def current_user(get_response):
    def wrapper(request):
        headers = request.headers
        print('---------------- START middleware current_user ----------------')
        for k, v in headers.items():
            print(f'{k.ljust(30)} ---> {v.ljust(80)}')
        print()
        print(f'session ---> {request.session._SessionBase__session_key}')
        print(f'path_info ---> {request.path_info}')
        print(f'current USER ---> {request.user}')
        # print(f'{request.user.backend}')
        # print(f'settings ---> {settings.__dict__}')
        print('---------------- END middleware current_user ----------------\n')
        result = get_response(request)
        return result
    return wrapper
