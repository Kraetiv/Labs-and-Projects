# CSC 323 Lab 0
# Alex Liang

import binascii
from collections import Counter
import codecs


# Task I

def asciiToHex(s):
    return binascii.hexlify(s.encode()).decode()

def base64ToHex(s):
    return codecs.encode(codecs.decode(s, 'base64'), 'hex')

def hexToBase64(s):
    return codecs.encode(codecs.decode(s, 'hex'), 'base64').strip()

#------------------------------------------------------------------------------------

# Task II

# A.
def byte_xor(s, key):
    l = len(s)
    byteKey = bytes([key] * l)
    return bytes([a ^ b for (a, b) in zip(s, byteKey)])
    
#Testing another way of xor-ing
def sb_xor(s, byte):
    return bytes([b ^ byte for b in s])

# B.
def scoreText(text):
    freq = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    n = len(text)
    c = 26

    # counts occurance of each letter
    for letter in alphabet:
        cnt = 0
        for ch in text:
            if ch == letter:
                cnt += 1
        freq.append(cnt)
    # summation variable
    total = 0

    # gets summation of ni(ni - 1) in total
    for i in range(len(freq)):
        ni = freq[i]
        total += ni * (ni - 1)

    # ic = total / ((N(N - 1)) / c)
    if n == 0:
        return 0
    ic = float(total) / ((n * (n - 1)) / c)

    return ic

def task_b():
    with open(r'C:\Users\2alex\CSC323\Lab00\Lab00_task_2.txt', 'r') as file:
        lines = file.readlines()
        count = 0
        '''
        Correct line = 40, key = 95, 
        string = out on bail fresh out of jail california dreaming * soon as i step on the scene im hearing ladies screaming
        
        '''
        

        # Checks which line has a score of more than 1 and prints out score, line, and key
        '''
        for i in range(256):
            count = 0
            for line in lines:
                b = bytes.fromhex(line)
                xored = sb_xor(b, i).decode('latin-1').lower()
                if scoreText(xored) > 1:
                    print(scoreText(xored), count, i)
                count += 1
        '''

        # Testing each key one by one
        b = bytes.fromhex(lines[40])
        print(sb_xor(b, 95).decode('latin-1').lower())

    file.close()


task_b()
    