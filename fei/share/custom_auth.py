"""一些认证、权限相关的功能
"""

def required_roles(func):
    """验证用户是否具有需要的role
    TODO: 
    """
    def wrapper(*args, **kwargs):
        # check if user have required roles
        return func(*args, **kwargs)
    return wrapper
