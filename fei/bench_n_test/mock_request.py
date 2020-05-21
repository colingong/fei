import sys
import urllib.request
import time

def func(url):
    response = urllib.request.urlopen(url).read()
    print(response)

if __name__ == '__main__':
    range_start = int(sys.argv[1])
    range_end = int(sys.argv[2])
    start = int(time.time())
    for id in range(range_start, range_end):
        url = f"http://127.0.0.1:8000/cache/cached/{id}/"
        func(url)
    end = int(time.time())
    print(start, end)
    print(f'--- used time : {end - start} s ---\n')