import numbers
from pydoc import plain
import sys
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Implementation of PKCS#7 Padding
def padData(data):
    if((len(data) % 16) != 0):
        bytesToPad = 16 - (len(data) % 16)
        arr = bytearray()

        for i in range(bytesToPad):
            arr.append(bytesToPad)
        data = data + arr

    return data

def submit(str, cipher, iv, key):
    lst = list(str)
    for i in range(len(lst)):
        if lst[i] == ';':
            lst[i] = "9"
        elif lst[i] == '=':
            lst[i] = "8"
    lst ="".join(lst)

    padded = padData(bytes("userid=456;userdata=" + lst + ";session-id=31337", 'utf-8'))
    numBlocks = int(len(padded) / 16)
    result = bytearray()

    for i in range(numBlocks):
        result.extend(cipher.encrypt(xor(padded[i * 16 : (16 + i * 16)], iv)))
        iv = cipher.encrypt(xor(padded[i * 16 : (16 + i * 16)], iv))
    return result

def xor(data, iv):
    return bytes(x ^ y for x, y in zip(iv, data))
    
#iv = get_random_bytes(16)
#key = get_random_bytes(16)
#cipher = AES.new(key, AES.MODE_ECB)
#submit("You're the man now, dog", cipher, iv, key)

def verify(str, cipher, iv, key):
    numBlocks = int(len(str) / 16)
    arr = bytearray()

    for i in range(numBlocks):
        decrypted = cipher.decrypt(str[i * 16 : 16 + i * 16])
        xored = xor(decrypted, iv)
        arr += xored
        iv = str[i * 16 : 16 + i * 16]
    return arr

def main():
    iv = get_random_bytes(16)
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_ECB)
    cipher2 = AES.new(key, AES.MODE_ECB)
    phrase = ";admin=true;"
    #5 11 16
    #4 10 15
    ciphertext = submit(phrase, cipher, iv, key)
    #print(ciphertext)
    xor1 = ord('=')^ord('8')
    xor2 = ord(';')^ord('9')

    ciphertext[4] = ciphertext[4] ^ xor2
    ciphertext[10] = ciphertext[10] ^ xor1
    ciphertext[15] = ciphertext[15] ^ xor2

    plaintext = verify(ciphertext, cipher2, iv, key)
    print(plaintext)


if __name__== "__main__":
    main()