# CSC 323 Lab 0
# Alex Liang

import binascii
import codecs
import base64
from collections import Counter


# Task I

def asciiToHex(s):
    return binascii.hexlify(s.encode()).decode()

def base64ToHex(s):
    return codecs.encode(codecs.decode(s, 'base64'), 'hex')

def hexToBase64(s):
    return codecs.encode(codecs.decode(s, 'hex'), 'base64')

#------------------------------------------------------------------------------------

# Task II

# D.
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

def shift(text, key):
    arr = []

    for i in range(len(text)):
        arr.append((text[i] - key[i % len(key)]) % 26)
    
    return arr

def task_d():
    with open(r'C:\Users\2alex\CSC323\Lab00\Lab0.TaskII.D.txt', 'r') as file:
        lines = file.read()

        c = Counter(lines)

        nums = []

        # Changes alphabets to nums 0-25
        for i in range(len(lines)):
            nums.append(ord(lines[i].lower()) - 97)        

        ''' 
        for size in range(2, 15):  
            test = [v for i, v in enumerate(nums) if i % size < 2]
            for i in range(26):
                for j in range(26):
                    shifted = shift(test, [i, j])

                    for k in range(len(shifted)):
                        shifted[k] = chr(shifted[k] + 97)

                    s = ''.join([str(elem) for elem in shifted])
                    
                    if scoreText(s) > 1.3:
                        print(size, i, j, scoreText(s))
        '''

        test = [v for i, v in enumerate(nums) if i % 14 < 14]

        for i in range(26):
            for j in range(26):
                #for l in range(26):
                
                    # add l in to test 3 at a time
                    shifted = shift(test, [12, 14, 12, 14, 13, 4, 24, 12, 14, 15, 17, 14, i, j])

                    for k in range(len(shifted)):
                        shifted[k] = chr(shifted[k] + 97)

                    s = ''.join([str(elem) for elem in shifted])

                    if scoreText(s) > 1.58:
                        # add l in to print 3 possible key bytes
                        print(i, j, scoreText(s), s)
        
                
        # keysize = 14, [12, 14, 12, 14, 13, 4, 24, 12, 14, 15, 17, 14, 1, 18]
        '''
        bigpoppanoinfoforthedeafederalagentsmadcauseimflagranttapmycellandthephone
        inthebasementmyteamsupremestaycleantriplebeamlyricaldreamibethatcatyouseeat
        alleventsbentgatsinholstersgirlsonshouldersplayboyitoldyameremicstomebruisetoomuchi
        losetoomuchsteponstagethegirlsbootoomuchiguessitscauseyourunwithlamedudestoomuch
        melosemytouchneverthatifididaintnoproblemtogetthegatwherethetrueplayersatthrowyour
        roliesintheskywaveemsidetosideandkeepyourhandshighwhileigiveyourgirltheeyeplayer
        pleaselyricallyfellasseebigbeflossingjigonthecoveroffortunedoubleoheresmyphonenumber
        yourmanaintgottoknowigotthedoughgottheflowdownpizatplatinumpluslikethizatdangerousontrizacksleaveyourassflizat
        '''


task_d()