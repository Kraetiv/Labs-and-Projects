import requests
import Crypto

def checkPadding(block):
    url = 'http://127.0.0.1:8080/'
    #numBlocks = int(len(ciphertext) / 32)
    #blocks = [None] * numBlocks
    #for i in range(numBlocks):
        #blocks[i] = bytes(ciphertext[i * 32: (i + 1) * 32], "UTF-8")

    arr = [0] * 16
    
    for i in range(1, 17):
        padding = [b ^ i for b in arr]

        for j in range(256):
            padding[-i] = j
            test = bytes(padding)
            #print(''.join(format(x, '02x') for x in test))
            
            query = 'enc=' + ''.join(format(x, '02x') for x in test) + block
            r = requests.get(url, params=query)

            if r.status_code != 403:
                break

        arr[-i] = j ^ i
        print(arr)
            

#checkPadding('5fdc4f0b7ca281d9b7c167450fcc3b7b')

#0bc6fe7a0b409192a854d62c712b8e86c997270e304d4d102495c0cdcaf43b125fdc4f0b7ca281d9b7c167450fcc3b7b


# Test last byte
# Last byte XOR 0x01 to get decrypted byte
# Change to next byte, append decrypted byte XOR 0x02

def decrypt(ct):
    arr = [233, 222, 0, 99, 16, 42, 34, 127, 64, 146, 199, 202, 205, 243, 60, 21]
    ct = [int(ct[x:2 + x], 16) for x in range(0, len(arr) * 2, 2)]  

    ans = ''


    for i in range(16):
        ans += chr(arr[i] ^ ct[i])

    print(ans)
    

decrypt(b'c997270e304d4d102495c0cdcaf43b12')
#a76b2089d18336601b4acb04cb8137bb