def fun(n):
    tprimes=[True for i in range(n+1)]
    p=2
    while(p*p<=n):
        if tprimes[p]:
            for i in range(p*p,n+1,p):
                tprimes[i]=False
        p=p+1
    arr=[]
    for i in range(2,n+1):
        if tprimes[i]:
            arr.append(i)
    return arr
#finds all the prime numbers less than this numbers
x=fun(1000000)
print(len(x))
print(x[10000])
