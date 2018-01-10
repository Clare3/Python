#More efficient prime number algorithm
import math
N=int(input("Find primes up to: "))
primes=(2,3)
i=4
while i<N:
    for k in range (0,len(primes)):
        j=primes[k]
        if i/j==int(i/j):
            i=i+1
            break
        elif j>math.sqrt(i):
            primes+=(i,)
            i=i+1
            break  
print("primes are: ",primes)
input("Press enter to exit")
