import sys
from hashlib import sha1

#Task II: SHA 1
def split(msg, skip):
    chunks = []
    for i in range(0, len(msg), skip):
        chunks.append(msg[i:i+skip])
    return chunks

def leftrotate(msg, count):
    return ((msg << count)|(msg >> (32 - count))) & 0xffffffff

def sha1Code(data, h0 = 0x67452301, h1 = 0xEFCDAB89, h2 = 0x98BADCFE, h3 = 0x10325476, h4 = 0xC3D2E1F0):
    #h0 = 0x67452301
    #h1 = 0xEFCDAB89
    #h2 = 0x98BADCFE
    #h3 = 0x10325476
    #h4 = 0xC3D2E1F0
    msg = ""

    # Sets message to binary/bits
    for i in range(len(data)):
        msg += '{0:08b}'.format(ord(data[i]))
    #print('msg: ', msg)
    
    ml = len(msg) # Length of original message
    #print(ml)

    # Add the bit '1' to message
    msg += '1'
    #print(msg)

    # Pads 0 until message length is congruent to 448 mod 512
    while len(msg) % 512 != 448:
        msg += '0'

    # Append ml, the original length as 64 bit big-endian
    # Length of bits should result in 512
    msg += '{0:064b}'.format(ml)
    
    # ^^^ ABOVE SHOULD BE CORRECT ^^^
    
    # Break message into 512-bit chunks
    for chunk in split(msg, 512):
        w = split(chunk, 32) # Creates a list of 16 32-bit words
        w = [int(i, 2) for i in w]

        while len(w) < 80:
              w.append(0)

        # Extend 16 32-bit words to 80 32-bit words
        # Limit leftrotate to return 32 bits since some are more than 32?
        for i in range(16, 80):
            w[i] = leftrotate((w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16]), 1) & 0xffffffff
        
        # Initialize hash value for this chunk:
        a = h0
        b = h1
        c = h2
        d = h3
        e = h4
        
        # Main loop
        for i in range(80):
            if 0 <= i <= 19:
                f = (b & c) ^ (~b & d)
                k = 0x5A827999
            elif 20 <= i <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= i <= 59:
                f = (b & c) ^ (b & d) ^ (c & d) 
                k = 0x8F1BBCDC
            elif 60 <= i <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = leftrotate(a, 5) + f + e + k + w[i] & 0xffffffff
            e = d
            d = c
            c = leftrotate(b, 30)
            b = a
            a = temp
        
        h0 = h0 + a & 0xffffffff
        h1 = h1 + b & 0xffffffff
        h2 = h2 + c & 0xffffffff
        h3 = h3 + d & 0xffffffff
        h4 = h4 + e & 0xffffffff

    hh = (h0 << 128) | (h1 << 96) | (h2 << 64) | (h3 << 32) | h4
    return hex(hh)[2:]



#print(sha1Code('The quick brown fox jumps over the lazy dog'))
#print(sha1Code('foo'))


# Finding Collision
def maskBits(str, bits):
    val = int(str, 16)
    mask = 1
    #mask = number of bits we want to get from val
    for i in range(bits):
        mask *= 2
    mask -= 1

    return val & mask

def compare(str1, str2):
    l = len(str1) // 2
    total = 0
    for i in range(l):
        if str1[i * 2] == str2[i * 2]:
            if str1[i * 2 + 1] == str2[i * 2 + 1]:
                total += 1
    return total

def collision(input, bits):
    count = 1
    hashed = maskBits(sha1Code(str(count) + input), bits)
 
    dict = {}

    while hashed not in dict:
        print(count)
        dict[hashed] = count
        count += 1
        
        hashed = maskBits(sha1Code(str(count) + input), bits)
    
    if hashed in dict:
        print("Collision: ", dict[hashed], count)
        print(maskBits(sha1Code(str(dict[hashed]) + input), bits))
        print(maskBits(sha1Code(str(count) + input), bits))

#print(collision('dog', 50))