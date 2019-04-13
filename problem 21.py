import math
majorsum=0
for n in range(2,10001):
    k=2
    tempsum=1
    while(k*k<=n):
        if n%k==0:
            if k!=n/k:
                tempsum+=k+int(n/k)
            else:
                tempsum+=k
        k+=1
    k=2
    divSum=tempsum
    tempsum=1
    while(k*k<=divSum):
        if divSum%k==0:
            if k!=divSum/k:
                tempsum+=k+int(divSum/k)
            else:
                tempsum+=k
        k+=1
    if n==tempsum and n!=divSum:
        majorsum+=n+divSum
        #print(n,divSum)
print(int(majorsum/2))
