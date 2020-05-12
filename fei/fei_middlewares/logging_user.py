"""记录当前访问的用户
"""
from django.conf import settings

def django_current_user(get_response):
    def wrapper(request):
        print('--- MIDDLEWARE [django_current_user] ----------------------')
        print(f'        session ---> {request.session._SessionBase__session_key}')
        print(f'        path_info ---> {request.path_info}')
        print(f'        current USER/ID ---> {request.user}/{request.user.id}')
        # print('------------------- END middleware [current_user] ---\n')
        result = get_response(request)
        return result
    return wrapper
