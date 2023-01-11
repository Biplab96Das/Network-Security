def inv_mod(a,m):
    r1,r2,t1,t2=m,a,0,1
    while (r2!=0):
        q=r1/r2
        r=r1%r2
        t=t1-q*t2
        r1=r2
        r2=r
        t1=t2
        t2=t
    if (t1>0):
        i=t1%m
        return i
    else:
        while (t1<0):
            mulF=1
            t1=t1+mulF*m
            mulF+=1
        i=t1%m
        return i
print("Hello Bob,select values for p and q")
p=input("p:")
q=input("q:")
n=int(p)*int(q)
phi_n=(int(p)-1)*(int(q)-1)
print("n="+str(n)+" "+"and"+" "+"phi_n="+str(phi_n))
print("Hello Bob,select the value of e,such that 1<=e<="+str(int(phi_n)-1))
e=input("e:")
d=inv_mod(int(e),int(n))
print("Hello Bob,The value of your private key is "+str(d))
p=input("Hello Alice,Enter the plaintext number:")
def bin_pow(x,y,m):
    res=pow(x,y)
    return res%m
c=bin_pow(int(p),int(e),int(n))
print("Hello Alice,sent the ciphertext to Bob which is = "+str(c))
print("I'm Bob,Alice has sent me the number which is = "+str(bin_pow(int(c),int(d),int(n))))
