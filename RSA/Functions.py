#Taegun Harshbarger
#Functions

import random

def modularExponentation(g,a,p):
    r = 1
    y = g%p
    while a > 0:
        if a&1 == 1:
            r = (r*y) % p
        y = y**2 % p
        a >>= 1
    return r

def millerRabin(n,k):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n-1)
        x = modularExponentation(a, s, n)
        if x == 1 or x == n-1:
            continue
        for _ in range(r-1):
            x = modularExponentation(x, 2, n)
            if x == n-1:
                break
        else:
            return False
    return True


def generatePrime(prime_bit):
    low = pow(2, prime_bit-1)
    high = pow(2, prime_bit)-1
    while True:
        rand_num = random.getrandbits(prime_bit)
        while rand_num not in range(low, high+1) or not rand_num%2:
            rand_num = random.getrandbits(prime_bit)
        if millerRabin(rand_num,64):
            return rand_num
#print(generatePrime(1024))