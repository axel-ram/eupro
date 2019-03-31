import math
#Classic method to find prime numbers below given number.
def prime(x):
    tprimes = [True for i in range(x+1)]
    p=2
    while(p*p<=x):
        if tprimes[p]:
            for i in range(p+p,x+1,p):
                tprimes[i]=False
        p+=1
    arr=[]
    for i in range(2,x+1):
        if tprimes[i]:
            arr.append(i)
    return arr
n=int(input())
arr=prime(n)
#print(arr)
result=1
#This section finds the highest exponent value of the prime factor that could be used in finding the lcm of series of 1 to n
for i in arr:
    a = math.floor(math.log(n)/math.log(i))
    print(a)
    result*=i**a
print(result)
