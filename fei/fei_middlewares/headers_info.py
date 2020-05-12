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

    Content-Type                   ---> text/plain
    Cookie                         ---> csrftoken=COuMh90BlYq4dOSxOqe9PzRo8frkH8lnPuviYvoSjxaqHRscHUWi4a95bLHlzAD8; sessionid=1h8ntp1x5mo7prtjnqbittnnhr413gcx
    Accept                         ---> text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    User-Agent                     ---> Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15
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

def response_header(get_response):
    def wrapper(request):
        result = get_response(request)
        # after
        print('--- MIDDLEWARE [response_header] ----------')
        for k, v in result._headers.items():
            print(f'        {str(k).ljust(30)} ---> {str(v).ljust(80)}')
        # print('---------- END   [response_header] ---')
        return result
    return wrapper