# CSC 323 Lab 0
# Alex Liang

import binascii
import codecs
import base64
import pprint


# Task I

def asciiToHex(s):
    return binascii.hexlify(s.encode()).decode()

def base64ToHex(s):
    return codecs.encode(codecs.decode(s, 'base64'), 'hex')

def hexToBase64(s):
    return codecs.encode(codecs.decode(s, 'hex'), 'base64')

#------------------------------------------------------------------------------------

# Task II

# A.
def byte_xor(s, key):
    l = len(key)
    return bytearray((s[i] ^ key[i % l]) for i in range(len(s)))
    
#Testing another way of xor-ing
def sb_xor(s, byte):
    return bytes([b ^ byte for b in s])


# C.
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

def task_c():
    with open(r'C:\Users\2alex\CSC323\Lab00\Lab0.TaskII.C.txt', 'r') as file:
        lines = file.read()
        b = base64.b64decode(lines)

        '''
        # Checks key length by grabbing i-th element in file (keylen = 15?)
        for size in range(2,22):
            test = [v for i, v in enumerate(b) if i % size < 1]
            for k in range(256):
                xored = sb_xor(test, k).decode('latin-1').lower()
                if scoreText(xored) > 1:
                    print(size ,k, scoreText(xored), xored)
        '''
    
        # the 10 is amount I skip, 2 is how much I grab
        test = [v for i, v in enumerate(b) if i % 10 < 10]
        '''
        for i in range(256):
            for j in range(256):
                xored = byte_xor(test, bytearray([97, 89])).decode('latin-1').lower()
                if scoreText(xored) > 1:
                    print(i, j, scoreText(xored), xored)
        '''
        for i in range(256):
            xored = byte_xor(test, bytearray([97, 121, 181, 231, 90, 97, 121, 149, 231, 122])).decode('latin-1').lower()
            if scoreText(xored) > 0.87:
                print(i, xored)

        
        # Key length = 10, key = (97, 121, 181, 231, 90, 97, 121, 149, 231, 122) ?

        '''
        one, two,three andto the fo
        snoop doggy dogg and dr. dre is at the door
        ready to make an entrance so back on up
        (cause you know we're about to rip stuff up)
        give me the microphone first so i can bust like a bubble*compton and long beach together 
        now you know you int rouble*ain't nothing but a gthang, baby
        two loc'ed out dudes so were crazy
        death row is the label that pays me
        unfadeable so please dont try to fade this
        '''

task_c()
