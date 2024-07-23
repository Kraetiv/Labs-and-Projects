from sha1 import *
from time import time
from requests import get
from hmac import compare_digest

def checkTime(bits): 
    url = 'http://127.0.0.1:8080/?q=foo&mac=' + bits
    #print(url)
    start = time()
    r = get(url)
    end = time()  
    return (end - start)

#checkTime('11')

timings = [(checkTime(f'6f04b5{i:02x}00000000000000000000000000000000'), f'{i:02x}') for i in range(256)]

#timings = []
#for i in range(256):
#    for j in range(256):
#        timings.append((checkTime(f'{i:02x}{j:02x}0000000000000000'), f'{i:02x}', f'{j:02x}'))

print(sorted(timings, reverse=True)[:15])
#6f04b560b98f0094a0f0b2039ceab88ea7539d0d


# One way to compare with constant time
def constant_time(a, b):
    return compare_digest(a, b)