#Taegun Harsharger
#Usage:python3 sha1.py

#Takes the message and breaks it into blocks
def parser(l, size): 
    return[l[i:i+size] for i in range(0,len(l),size)]

def rotl(x, n):
    return ((x << n) | (x >> (32 - n))) &  0xffffffff 

#Preprocessing
def preprocessing(m):
    
    bitPaddedM = ''.join('{0:08b}'.format(ord(c), 'b') for c in m)

    l = len(bitPaddedM)
    bitPaddedM += '1'

    while(len(bitPaddedM) % 512 != 448):
        bitPaddedM += '0'
    
    bitPaddedM += '{0:064b}'.format(l) #len in 64-bit block

    #Parse message into 512 bit blocks
    block = parser(bitPaddedM, 512)
    return(block)


def sha1(m):
    #Initial hash value (H0) in hex
    h=[0x67452301,0xEFCDAB89,0x98BADCFE,0x10325476,0xC3D2E1F0]

    blocks=preprocessing(m)

    #Prepare message schedule
    for block in blocks:
        #Parse into 32 bit blocks
        smallBlock = parser(block, 32)
        w = [0] * 80

        for t in range(80):
            if 0<= t <=15:
                w[t] = int(smallBlock[t], 2)
            elif 16 <= t <= 79:
                w[t] = rotl((w[t-3] ^ w[t-8] ^ w[t-14] ^ w[t-16]), 1)
        
        #Initialize five working variables with hash value
        a = h[0]
        b = h[1]
        c = h[2]
        d = h[3]
        e = h[4]

        #For t=0 to 79
        for t in range(80):
            if 0 <= t <= 19:
                k = 0x5A827999 #Given constants of k
                f = (b & c) | ((~b) & d)

            elif 20 <= t <= 39:
                k = 0x6ED9EBA1
                f = b ^ c ^ d

            elif 40 <= t <= 59:
                k = 0x8F1BBCDC
                f = (b & c) | (b & d) | (c & d)

            elif 60 <= t <= 79:
                k = 0xCA62C1D6
                f = b ^ c ^ d

            T=rotl(a,5) + f + e +k +w[t] &0xffffffff
            e = d
            d = c
            c = rotl(b,30)
            b = a
            a = T
        #Compute ith hash value
        h[0] = h[0] + a & 0xffffffff
        h[1] = h[1] + b & 0xffffffff
        h[2] = h[2] + c & 0xffffffff
        h[3] = h[3] + d & 0xffffffff
        h[4] = h[4] + e & 0xffffffff

    return '%08x%08x%08x%08x%08x' % (h[0], h[1], h[2], h[3], h[4])


output = sha1("This is a test of SHA-1.")
print(output)
output = sha1("Kerckhoff's principle is the foundation on which modern cryptography is built.")
print(output)
output = sha1("SHA-1 is no longer considered a secure hashing algorithm.")
print(output)
output = sha1("SHA-2 or SHA-3 should be used in place of SHA-1.")
print(output)
output = sha1("Never roll your own crypto!")
print(output)