from rest_framework import authentication

def drf_user_info(get_response):
    def wrapper(request):
        result = get_response(request)
        try:
            user, token = authentication.TokenAuthentication().authenticate(request)
            print(f'--- START [drf_user_inf: ID /User / Token] ---> {user.id} / {user} / {token}')
        except:
            print(f'--- [START [drf_user_inf] AUTH FAILED!')

        return result
    return wrapper