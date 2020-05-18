"""检查request / response 的headers
    用于debug
"""
from django.conf import settings

def request_headers(get_response):
    """
    下面这几个常规的headers不显示:
        Content-Length                 --->
        Referer                        ---> http://127.0.0.1:8000/v2/
        Connection                     ---> keep-alive
        Host                           ---> 127.0.0.1:8000
        Upgrade-Insecure-Requests      ---> 1

    下面这几个headers会被显示
        Content-Type                   ---> text/plain
        Cookie                         ---> csrftoken=COuMh90BlYq4dOSxOq ...; sessionid=1h8ntp1x ...
        Accept                         ---> text/html,application/xht ...
        User-Agent                     ---> Mozilla/5.0 (Macintosh; Intel Mac OS X 1 ...
        Accept-Language                ---> en-us
        Accept-Encoding                ---> gzip, deflate
        request.user.id ---> 25
    """

    def wrapper(request):
        headers_not_log = ["Content-Length", "Referer", "Connection", "Host", "Upgrade-Insecure-Requests", ]
        headers = getattr(request, 'headers', 'request目前还没有 *headers* ')
        print('--- MIDDLEWARE [request_headers] ----------------')
        for k, v in headers.items():
            if k not in headers_not_log:
                print(f'        {k.ljust(30)} ---> {v.ljust(80)}')
        # print('---------------- END middleware [request_headers] ---\n')
        result = get_response(request)
        return result
    return wrapper

def response_headers(get_response):
    """显示response的headers

        和request_headers类似，但这里显示的是reponse headers
    """
    def wrapper(request):
        result = get_response(request)
        # after
        print('--- MIDDLEWARE [response_header] ----------')
        for k, v in result._headers.items():
            print(f'        {str(k).ljust(30)} ---> {str(v).ljust(80)}')
        # print('---------- END   [response_header] ---')
        return result
    return wrapper