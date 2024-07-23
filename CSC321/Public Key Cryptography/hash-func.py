from bisect import bisect_right
import hashlib
import time
import numbers
import sys
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def hash(input):
    return hashlib.sha256(input.encode('utf-8')).hexdigest()

def truncate(str1, bits):
    val = int(str1, 16)
    mask = 1

    #mask = number of bits we want to get from val
    for i in range(bits):
        mask *= 2
    mask -= 1

    return val & mask

def compare(str1, str2):
    l = len(str1) // 2
    total = 0
    for i in range(l):
        if str1[i * 2] == str2[i * 2]:
            if str1[i * 2 + 1] == str2[i * 2 + 1]:
                total += 1
    return total

def collision(input, bits):
    count = 1
    print(hash(str(count) + input))
    hashed = truncate(hash(str(count) + input), bits)
 
    dict = {}

    start = time.time()
    while hashed not in dict:
        dict[hashed] = 1
        count += 1
        
        hashed = truncate(hash(str(count) + input), bits)

    end = time.time()
    print(count)
    return end - start

def main():
    print(collision('dog', 8))

if __name__== "__main__":
    main()