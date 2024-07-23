import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

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

def xor(data, iv):
    return bytes(x ^ y for x, y in zip(iv, data))

def decrypt(str, cipher, iv, key):
    numBlocks = int(len(str) / 16)
    arr = bytearray()

    for i in range(numBlocks):
        decrypted = cipher.decrypt(str[i * 16 : 16 + i * 16])
        xored = xor(decrypted, iv)
        arr += xored
        iv = str[i * 16 : 16 + i * 16]
    return arr

def encrypt(file, key, iv):
    f = open(file, 'rb')
    output = b""
    lines = f.read()

    padded = pad(lines)


    cipher = AES.new(key, AES.MODE_ECB)

    numBlocks = int(len(padded) / 16)

    for i in range(numBlocks):
        output += (cipher.encrypt(xor(padded[i * 16 : (16 + i * 16)], iv)))
        
        iv = cipher.encrypt(xor(padded[i * 16 : (16 + i * 16)], iv))

    print(base64.b64encode(output))
    f.close()

def decrypt(file, key, iv):
    f = open(file, 'rb')
    output = b""
    lines = base64.b64decode(f.read())
    cipher = AES.new(key, AES.MODE_ECB)

    numBlocks = int(len(lines) / 16)
    arr = bytearray()

    for i in range(numBlocks):
        decrypted = cipher.decrypt(lines[i * 16 : 16 + i * 16])
        xored = xor(decrypted, iv)
        arr += xored
        iv = lines[i * 16 : 16 + i * 16]
    print(unpad(arr))

    f.close()



 
#encrypt(r'C:\Users\2alex\CSC323\Lab02\test2.txt', b"inputsecretkey00", b"enterrandomivval")
decrypt(r'C:\Users\2alex\CSC323\Lab02\Lab2.TaskIII.A.txt', b"MIND ON MY MONEY", b"MONEY ON MY MIND")