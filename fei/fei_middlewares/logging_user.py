"""记录当前访问的用户
"""
from django.conf import settings

def django_current_user(get_response):
    """记录当前访问的用户

        django用户，非drf用户
    """
    def wrapper(request):
        print('--- MIDDLEWARE [django_current_user] ----------------------')
        print(f'        session ---> {request.session._SessionBase__session_key}')
        print(f'        path_info ---> {request.path_info}')
        print(f'        current USER/ID ---> {request.user}/{request.user.id}')
        # print('------------------- END middleware [current_user] ---\n')
        result = get_response(request)
        return result
    return wrapper

from app_models.models import UserLog

def logging_user(get_response):
    """
    HTTP_X_FORWARDED_FOR
    HTTP_X_REAL_IP
    REMOTE_ADDR
    """
    def wrapper(request):
        user_log = UserLog()
        print(f'USER:               {request.user.username}')
        print(request.path_info)
        try:
            print(f'REMOTE_ADDR:        {request.META.get("REMOTE_ADDR")}')
        except:
            pass

        try:
            print(f'X_REAL_IP:          {request.META.get("HTTP_X_REAL_IP")}')
        except:
            pass

        try:
            print(f'X_FORWARDED_FOR:    {request.META.get("HTTP_X_FORWARDED_FOR")}')
        except:
            pass

        result = get_response(request)
        return result
    return wrapper