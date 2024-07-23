import numbers
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Implementation of PKCS#7 Padding
def padData(data):
    if((len(data) % 16) != 0):
        bytesToPad = 16 - (len(data) % 16)
        arr = bytearray()

        for i in range(bytesToPad):
            arr.append(bytesToPad)
        print(arr)
        data = data + arr

    return data

def main():
    f = open(r"C:\Users\2alex\CSC321\Symmetric_Crypto\cp-logo.bmp", 'rb')
    result = open('ecbEncrypted.bmp', 'wb')
    logo = f.read()
    print(logo)

    header = logo[0:54] # Takes header for bmp
    result.write(header)

    body = logo[54:] # Takes body of bmp
    print(body)
    paddedBody = padData(body)
    
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_ECB)

    numBlocks = int(len(paddedBody) / 16)

    for i in range(numBlocks):
        result.write(cipher.encrypt(paddedBody[i * 16 : (16 + i * 16)]))


if __name__== "__main__":
    main()