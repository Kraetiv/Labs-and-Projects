import base64
from Crypto.Cipher import AES
import requests

# Implementation of PKCS#7 Padding
def pad(data):
    if((len(data) % 16) != 0):
        bytesToPad = 16 - (len(data) % 16)
        arr = bytearray()

        for i in range(bytesToPad):
            arr.append(bytesToPad)
        data = data + arr

    return data

def unpad(data):
    if len(data) % 16 != 0:
        return "Invalid Padding"
    l = len(data)
    numBlocks = data[l - 1]
    return data[:l - numBlocks]

# Encrypt function for ECB
def ecb_encrypt(key, file):
    f = open(file, 'rb')
    output = b""
    lines = f.read()
    print(lines)
    padded = pad(lines)

    cipher = AES.new(key, AES.MODE_ECB)
    numBlocks = int(len(padded) / 16)

    for i in range(numBlocks):
       output += (cipher.encrypt(padded[i * 16 : (16 + i * 16)]))
       
    print(base64.b64encode(output))
    f.close()

# Decrypt function for ECB
def ecb_decrypt(key, file):
    f = open(file, 'r')
    output = ""
    lines = base64.b64decode(f.read())
    #print(lines)
    cipher = AES.new(key, AES.MODE_ECB)
    decoded = cipher.decrypt(lines)
    output = open(r'C:\Users\2alex\CSC323\Lab02\test.txt', 'wb')
    output.write(unpad(decoded))

    f.close()

# Function to find the correct bmp
def findBmp(file):
    f = open(file, 'r')
    lines = f.readlines()
    
    count = 0

    for line in lines:
        line.strip('\n')
        decoded = bytes.fromhex(line)
        fileName = 'test' + str(count) + '.bmp'
        output = open(fileName, 'wb')
        output.write(decoded)
        count += 1

# Cookie example: de2d28f70f751a4286d480ee47c2c4a7e1d9a928a96512b9449cab347566fa68
# '=' = 28?
#user=user&uid=UID&role=user


#ecb_encrypt(b"CALIFORNIA LOVE!", r'C:\Users\2alex\CSC323\Lab02\test.txt')
ecb_decrypt(b"CALIFORNIA LOVE!", r'C:\Users\2alex\CSC323\Lab02\Lab2.TaskII.A.txt')
#findBmp(r'C:\Users\2alex\CSC323\Lab02\Lab2.TaskII.B.txt')