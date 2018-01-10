#Eudlid's algorithm to find the hcm of a and b
a=int(input("a= "))
b=int(input("b= "))
if a>b:
    c=a
    a=b
    b=c
#so that now a is less than or equal to b
r=1
while r>0:
    q=1
    while b>=q*a:
        q=q+1
    r=b-(q-1)*a
    print(b,"=",q-1,"*",a,"+",r)
    b=a
    a=r
print(b)

