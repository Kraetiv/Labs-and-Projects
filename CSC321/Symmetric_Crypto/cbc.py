import numbers
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

def xor(data, iv):
    return bytes(x ^ y for x, y in zip(iv, data))

def main():
    f = open("cp-logo.bmp", 'rb')
    result = open('cbcEncryted.bmp', 'wb')
    logo = f.read()

    header = logo[0:54] # Takes header for bmp
    result.write(header)

    body = logo[54:] # Takes body of bmp
    paddedBody = padData(body)
    
    iv = get_random_bytes(16)
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_ECB)

    numBlocks = int(len(paddedBody) / 16)

    for i in range(numBlocks):
        result.write(cipher.encrypt(xor(paddedBody[i * 16 : (16 + i * 16)], iv)))
        iv = cipher.encrypt(xor(paddedBody[i * 16 : (16 + i * 16)], iv))
    


if __name__== "__main__":
    main()