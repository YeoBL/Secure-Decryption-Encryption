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
readfile="encrypted.txt"
rval=""
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), readfile), 'r') as f:
    s2=f.read()
tmp=s2.split('\n')
s+=tmp[0]
s2=s2[len(tmp[0])+1::]
key=input("Enter the password: ")
d={}
skey=rnum(len(s),len(s)-96,len(s2),len(key),abs(len(s2)-len(s)),checksum(s),checksum(key))
r.seed(skey)
shuffle=r.sample(range(0,len(s2)),len(s2))
s2=shuffle_backward(s2,shuffle)
for i in range(0,len(s)):
    d[s[i]]=i
for i in range(0,len(s2)):
  n=d[s2[i]]
  rval+=s[(n-d[key[i%len(key)]]+len(s))%len(s)]
writefile="decrypted.txt"
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), writefile), 'w') as f:
    f.write(rval)
