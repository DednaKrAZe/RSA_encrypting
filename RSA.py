def gcdex(a,b):
    if b==0:
        return a,1,0
    else:
        d,x,y=gcdex(b,a%b)
        return d,y,x-y*(a//b)
def keys():
    p=29873
    q=96959
    n=p*q
    eiler=(p-1)*(q-1)
    ex=257
    d=gcdex(eiler,ex)[2]%eiler
    openkey=[ex,n]
    secretkey=[d,n]
    return [openkey,secretkey]
def degree(x,e,n):
    if (e==0):
        return 1
    z=degree(x,e//2,n)
    if (e%2==0):
        return (z*z)%n
    else:
        return (x*z*z)%n

def encrypting(text):
    key=keys()[0]
    crypted=''
    for i in text:
        x=ord(i)
        xnew=degree(x,key[0],key[1])
        crypted+=str(xnew)+"|"
    return crypted

def decrypting(text):
    txt=list(text.split('|'))
    decrypted=''
    key=keys()[1]
    for i in txt:
        if i!="":
            xnew=chr(degree(int(i),key[0],key[1]))
            decrypted+=xnew
    return decrypted

print("Открытый и закрытый ключ: ",keys())
print(encrypting("Lorem ipsum"))
print(decrypting(encrypting("Lorem ipsum")))
