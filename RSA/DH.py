# Taegun Harshbarger
# Diffie-Hellman
from ctypes import sizeof
import Functions
import random
import hashlib
import math
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
"""
prime=Functions.generatePrime(1024)
i=0
while(Functions.millerRabin(int(((prime-1)//2)),64)!=True):
    prime=Functions.generatePrime(1024)
    print(prime)
    print(i)
    i+=1
"""
prime=138537871036119104086587974093086539015367281399251420228105965441773206895871797021228570750092565372742619668911143164839284919449973494319950346159292518460699077918254478924843669005900406437299958319149017515744266338364592011745164421951231948873641946739308638052661373287914419822314624380877442412839
#print("prime")
#print(prime)
a=42
print("a")
print(a)
print("Public Key")
#g^a used for the website function
ga=Functions.modularExponentation(5,a,prime)
print(ga)
#given g^b from the website
gb=39104340664846640250489317506949022312016335206357389483124884761086269862134564435069495979377474818854221081823832257682543952426969441166471306783617208689357948521108486415917096287462662312840865860425203985228459950380152587815458234623095642414128235355840973277936468103456239021726847695651797660225

print("DHKey")
DHKey=Functions.modularExponentation(gb,a,prime)
print(DHKey)

hash=hashlib.sha256(DHKey.to_bytes(math.ceil((math.floor(math.log2(DHKey)) + 1) // 8) + 1, 'big'))
digest=hash.digest()
key=digest[:16]
print(key)
decrypted = AES.new(
        key=key,
        mode=AES.MODE_CBC,
        IV=bytes.fromhex('1a94bb1133190d0faecf1f1072a59a52')
    ).decrypt(bytes.fromhex('fe821627fbdbfd0fe40cdd64469ef037bc0b927a8cefef16d12f141b31f92b4f26515d31b9793f1a8a58c31690ab68a3ad522c7532196e69d8777f07ec35ce33e9cc642c910348e7e3008bdf0b5e255ce89f94881ff8a6e8171ebeaf4d590b67677e7b4c5955d3612b480222fccde386b1782f488c3eea693a4175e4d7fc665d335b71ebaabcd5b04db7f6e46f84726ee8171bbe2afa4dab1876ee302f3b1851'))
