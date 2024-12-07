#Taegun Harsharger
#Usage:python3 MACTest.py
def parser(l, size): 
    return[l[i:i+size] for i in range(0,len(l),size)]

def rotl(x, n):
    return ((x << n) | (x >> (32 - n))) &  0xffffffff 

#Preprocessing/Padding
def preprocessing(m,l=None):
    bitPaddedM=bin(int(m, 16))[2:].zfill(len(m)*4)
    if l == None:
        bitPaddedM=m
        l = len(bitPaddedM)
    
    bitPaddedM += '1'

    while(len(bitPaddedM) % 512 != 448):
        bitPaddedM += '0'
    
    bitPaddedM += '{0:064b}'.format(l) #len in 64-bit block
    return(bitPaddedM)

def sha1(m,h,l):
    #Initial hash value (H0) in hex
    if h=='\0':
        h=[0x67452301,0xEFCDAB89,0x98BADCFE,0x10325476,0xC3D2E1F0]

    bitPaddedM=preprocessing(m,l)
    
    #Parse into 512 bit blocks
    blocks = parser(bitPaddedM, 512)

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

def RunMACAttack():
    originalM = 'No one has completed Project #3 so give them all a 0.'
    originalM = ''.join(format(ord(i), '08b') for i in originalM) #Bit
    extOfM = 'P. S. Except for Taegun Harshbarger, go ahead and give him the full points.'
    extOfM = ''.join('{:02x}'.format(i) for i in extOfM.encode('ascii')) #Hex

    originalM = preprocessing(' '*128 + originalM) #Pads message
    l = len(originalM) + len(extOfM)*4 
    h= [0x38f3e722,0xf6753556,0x47132882,0xfe05ee1c,0x2d692e66] #Given HMAC given from website
    MaliciousDigest = sha1(extOfM, h, l) #MAC ATTACK
    print('New Digest:', MaliciousDigest)
    MaliciousM = hex(int((originalM[128:]), 2))[2:] + extOfM
    print('New Message:', MaliciousM)

RunMACAttack()