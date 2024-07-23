import hashlib
import numbers
import sys
from Crypto.Util.number import getPrime
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def euclidean_alg(n1, n2):
    if n1 == 0:
        return (n2, 0, 1)
    else:

        # g = gcd(n1, n2) and n1*x + n2*y = g
        g, y, x = euclidean_alg(n2 % n1, n1)
        return (g, x - (n2 // n1) * y, y)

def modInv(n1, n2):
    g, x, y = euclidean_alg(n1, n2)
    return x % n2

def encrypt(m, e, n):
    return (m ** e) % n

def decrypt(c, d, n):
    return (c ** d) % n

def generateKey(n):
    p = getPrime(n)
    q = getPrime(n)
    print(q)
    e = 37
    d = 0
    msg = 'Does this work?'
    int_msg = [ord(ch) for ch in msg]

    n = p * q
    phi_n = (p - 1) * (q - 1)

    d = modInv(e, phi_n) 

    #encrypted = [encrypt(m, e, n) for m in int_msg]
    #print(encrypted)

    #decrypted = [decrypt(c, d, n) for c in encrypted]
    #print(decrypted)


def main():
    generateKey(128)


if __name__== "__main__":
    main()