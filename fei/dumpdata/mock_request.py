import urllib.request

def func(url):
    response = urllib.request.urlopen(url).read()
    print(response)

if __name__ == '__main__':
    for id in range(100, 200):
        url = f"http://127.0.0.1:8000/cache/cached/{id}/"
        func(url)