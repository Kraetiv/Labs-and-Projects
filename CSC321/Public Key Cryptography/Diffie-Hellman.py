import hashlib
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
    p = 37
    g = 1
    a = 4 # random private key for Alice
    b = 3 # random private key for Bob

    p_str = ("B10B8F96" "A080E01D" "DE92DE5E" "AE5D54EC" "52C99FBC" "FB06A3C6"
            "9A6A9DCA" "52D23B61" "6073E286" "75A23D18" "9838EF1E" "2EE652C0"
            "13ECB4AE" "A9061123" "24975C3C" "D49B83BF" "ACCBDD7D" "90C4BD70"
            "98488E9C" "219A7372" "4EFFD6FA" "E5644738" "FAA31A4F" "F55BCCC0"
            "A151AF5F" "0DC8B4BD" "45BF37DF" "365C1A65" "E68CFDA7" "6D4DA708"
            "DF1FB2BC" "2E4A4371"
            )
    p_str = int(p_str, 16)
    
    g_str = ("A4D1CBD5" "C3FD3412" "6765A442" "EFB99905" "F8104DD2" "58AC507F"
            "D6406CFF" "14266D31" "266FEA1E" "5C41564B" "777E690F" "5504F213"
            "160217B4" "B01B886A" "5E91547F" "9E2749F4" "D7FBD7D3" "B9A92EE1"
            "909D0D22" "63F80A76" "A6A24C08" "7A091F53" "1DBF0A01" "69B6A28A"
           "D662A4D1" "8E73AFA3" "2D779D59" "18D08BC8" "858F4DCE" "F97C2A24"
            "855E6EEB" "22B3B2E5"
            )
    g_str = int(g_str, 16)

    # Actual Alice and Bob A and B
    A = (g ^ a) % p
    B = (g ^ b) % p

    s = (B ^ a) % p # 2

    iv = get_random_bytes(16)
    h = hashlib.sha256()
    h.update(b'2')
    key = h.digest()[:16]

    cipher = AES.new(key, AES.MODE_CBC, iv)
    msg = padData('Hi Bob!'.encode('utf-8'))

    encrypted = cipher.encrypt(msg)

    cipher2 = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher2.decrypt(encrypted)

if __name__== "__main__":
    main()