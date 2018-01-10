#Finds all of the primes up to a given N
import math
N=int(input("largest possible prime= "))
print("2\n3")
for i in range(4, N):
    j=2
    k=i/j
    while int(k)!=k:
        if j>int(math.sqrt(i)):
            print(i)
            break
        else:
            j=j+1
            k=i/j
input("press the enter key to exit")
