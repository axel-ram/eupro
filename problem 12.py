import math
arr=[]
#find all the prime numbers below 1000
tprimes = [True for i in range(1001)]
p=2
while(p*p<=1000):
    if tprimes[p]:
        for i in range(p+p,1001,p):
            tprimes[i]=False
    p+=1
for i in range(2,1001):
    if tprimes[i]:
        arr.append(i)
def nods(number):
    sqrt=int(math.sqrt(number))
    count=1
    for k in arr:
        exp=1
        condition=False
        while(number%(k**exp)==0):
            exp+=1
            condition=True
        if condition:
            count*=exp
    return (count)

n=10000
while(nods(n*(n+1)//2)<500):
    n+=1
#print(nods(36))
print(n*(n+1)//2)
