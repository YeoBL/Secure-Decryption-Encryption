import os
import random as r
import hashlib
def checksum(s):
    a = hashlib.md5(s.encode())
    b = a.hexdigest()
    as_int=int(b,16)
    return as_int
def shuffle_forward(s,order):
    s2=''
    for i in order:
        s2+=s[i]
    return s2
def shuffle_backward(s,order):
    d={}
    n=0
    for i in order:
        d[i]=n
        n+=1
    s2=''
    for i in range(0,len(s)):
        s2+=s[d[i]]
    return s2
def decimalToBinary(n):
    return bin(n).replace("0b", "")
def mod(a,b,m):
    ans=1
    b=str(decimalToBinary(b))[::-1]
    for i in b:
        if i=='1':
            ans=(ans*a)%m
        a=(a*a)%m
    return ans
def rnum(*args):
    cur=args[0]
    for i in range(0,len(args)):
        if not i:
            continue
        cur=mod(cur,i,1e9+7)
    return int(cur)
s='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \n'
readfile="decrypted.txt"
rval=""
rval2=""
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), readfile), 'r') as f:
    s2=f.read()
for i in s2:
    if i not in s:
        s+=i
        rval+=i
rval+='\n'
key=input("Create a password: ")
d={}
skey=rnum(len(s),len(s)-96,len(s2),len(key),abs(len(s2)-len(s)),checksum(s),checksum(key))
for i in range(0,len(s)):
    d[s[i]]=i
for i in range(0,len(s2)):
    j=s2[i]
    rval2+=s[(d[key[i%len(key)]]+d[j])%len(s)]
writefile="encrypted.txt"
r.seed(skey)
shuffle=r.sample(range(0,len(rval2)),len(rval2))
rval2=shuffle_forward(rval2,shuffle)
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), writefile), 'w') as f:
    f.write(rval+rval2)
