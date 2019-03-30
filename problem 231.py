import math
n,m=map(int,input().split())
#(nCm)=mul(n to m+1)/(n-m)!
tprimes=[True for i in range(n+1)]

#Sieve of Eratosthenes
#find all the prime numbers below n

p=2
while(p*p<=n):
    if tprimes[p]:
        for i in range(p*p,n+1,p):
            tprimes[i]=False
    p+=1

#collect all the prime numbers
arrPrimes=[]
for i in range(2,n+1):
    if tprimes[i]:
        arrPrimes.append(i)
#print(len(arrPrimes))

#3 lists to store the max exponent of primes that can divide the factorial of n.m,n-m
arr1=[0 for _ in range(n+1)]
arr2=[0 for _ in range(n+1)]
arr3=[0 for _ in range(n+1)]


for i in arrPrimes:
    count=1
    while(n//(i**count)):
        arr1[i]+=n//(i**count)
        #print(n//(i**count))
        count+=1
        
for i in arrPrimes:
    count=1
    while(m//(i**count)):
        arr2[i]+=m//(i**count)
        count+=1

for i in arrPrimes:
    count=1
    while((n-m)//(i**count)):
        arr3[i]+=(n-m)//(i**count)
        count+=1

#find the prime factorization of nCr
diff = [a1 - (a2+a3) for a1, a2,a3 in zip(arr1, arr2, arr3)]

#for i in range(2,10):
#    print(i,arr1[i],arr2[i],arr3[i],diff[i])

#sum of the terms of prime factorization
sum=0
for i in range(2,n+1):
        sum+=i*diff[i]
        #print(sum,i)
#print(diff)
print(sum)
    
