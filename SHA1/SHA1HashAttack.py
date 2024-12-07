# Taegun Harshbarger
# Usage:python3 SHA1HashAttack.py <String to Hash> <Number of Bits>

import hashlib
import random
import secrets
import string
import sys
from statistics import mean

def HashAttack(user_string, bitSize):
    runs = [] #Collison
    samples = 0
    while samples < 50:
        run = 0
        hashList = [SHA1Hash(user_string,bitSize)]
        hash = 0
        while hash not in hashList:
            hashList.append(hash)
            hash = SHA1Hash(RandomString(),bitSize)
            run += 1
        runs.append(run)
        samples += 1

    print("Collision:{}".format(bitSize))                                                                                                
    for run in runs:
        print(run)
    print(mean(runs))

##################################################################

    runs = [] #Preimage
    samples = 0
    while samples < 50:
        run = 0
        randomHash = 0
        while randomHash != SHA1Hash(user_string,bitSize):
            run += 1
            randomHash = SHA1Hash(RandomString(),bitSize)
        runs.append(run)
        samples += 1

    print("PreImage:{}".format(bitSize))
    for run in runs:
        print(run)
    print(mean(runs))

def SHA1Hash(str,bitSize):
    sha1 = hashlib.sha1(str)
    hash = int.from_bytes(bytearray(sha1.digest()), 'big')
    return hash & int('1'*bitSize,2)

def RandomString():
    rand = ''.join(secrets.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for i in range(random.randint(5, 8)))
    return rand.encode('utf-8')

def main(argv):
    HashAttack(argv[0].encode('utf-8'), int(argv[1]))

if __name__ == '__main__':
    main(sys.argv[1:])