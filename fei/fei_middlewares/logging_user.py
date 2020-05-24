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
    """日志记录到日志表

    'x_forwarded_for',
    'x_real_ip',
    'remote_addr',
    'userid',
    'username',
    'datetime',
    'url',
    'method',
    'payload',
    """
    def wrapper(request):
        user_log = UserLog()
        if request.META.get('HTTP_X_FORWARDED_FOR'):
            user_log.x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        else:
            user_log.x_forwarded_for = request.headers.get('X_FORWARDED_FOR')

        if request.META.get('HTTP_X_REAL_IP'):
            user_log.x_real_ip = request.META.get('HTTP_X_REAL_IP')
        else:
            user_log.x_real_ip = request.headers.get('X_REAL_IP')

        if request.META.get('REMOTE_ADDR'):
            user_log.remote_addr = request.META.get('REMOTE_ADDR')
    
        if request.user.userid:
            user_log.userid = request.user.id

        if request.user.username:
            user_log.username = request.user.username

        user_log.url = request.path_info
        user_log.method = request.method
        user_log.save()

        result = get_response(request)
        return result
    return wrapper