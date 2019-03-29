n=int(input())
#standard Sieve Of Eratosthenes method to find all the prime number below given number
tprimes=[True for i in range(n+1)]

p=2
while(p*p<=n):
    if tprimes[p]:
        for i in range(p*p,n+1,p):
            tprimes[i]=False
    p+=1
#find summation of all prime numbers
sum=0
for i in range(2,n+1):
    if tprimes[i]:
        sum+=i

print(sum)
