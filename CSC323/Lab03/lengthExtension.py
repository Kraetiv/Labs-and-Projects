import requests
from sha1 import sha1Code

def attack(msg, hash):
    l = len(msg)
    padLength = 64 - l
    print(padLength)



def getRegisters(hash):
    return [hash >> 128, (hash >> 96) & 0xffffffff, (hash >> 64) & 0xffffffff, (hash >> 32) & 0xffffffff, hash & 0xffffffff]

attack('Funny names?', 'ff7c8913fc9a883a1ec59360fcc17685ba4b9604')
print(getRegisters(int('ff7c8913fc9a883a1ec59360fcc17685ba4b9604', 16)))
#Funny names?
#ff7c8913fc9a883a1ec59360fcc17685ba4b9604