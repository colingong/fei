"""检查一些信息，尤其是request
"""
from django.conf import settings

def request_info(get_response):
    def wrapper(request):
        headers = getattr(request, 'headers', 'request目前还没有 *headers* ')
        print('---------------- START middleware 检查信息 ----------------')
        # print(f'headers ---> {headers}')
        for k, v in headers.items():
            print(f'{k.ljust(30)} ---> {v.ljust(80)}')
        # print(f'request.user.__dict__ ---> {request.user.__dict__}')
        print(f'request.user.id ---> {request.user.id}')
        # print(f'dir(request.user) ---> {dir(request.user)}')
        # print(f'request.user.__dir__ ---> {request.user.__dir__()}')
        # for k, v in request.user.items():
        #     print(k, v)


        print('---------------- END middleware 检查信息 ----------------\n')
        result = get_response(request)
        return result
    return wrapper
