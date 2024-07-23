import requests
import Crypto

def check():
    url = 'http://127.0.0.1:8080/'
    #numBlocks = int(len(ciphertext) / 32)
    #blocks = [None] * numBlocks
    #for i in range(numBlocks):
        #blocks[i] = bytes(ciphertext[i * 32: (i + 1) * 32], "UTF-8")

    
    for i in range(256):
        c1 = f'0000000000000000000000000000{i:02x}b9' + '542473dbea464ae6f866181f4957e70d'

        query = 'enc=' + c1
        r = requests.get(url, params=query)

        if r.status_code == 404:
            print(i)
            
            

check()

# 305d4b8f87c1326572bb0a83c2bb0c00ee4c4da9b6ec5904324dcc03cc8630bc542473dbea464ae6f866181f4957e70d
# bb
# [167, 107, 32, 137, 209, 131, 54, 96, 27, 74, 203, 4, 203, 129, 55, 187]

# Test last byte
# Last byte XOR 0x01 to get decrypted byte
# Change to next byte, append decrypted byte XOR 0x02