arr=[]
n=100
for i in range(n):
    arr.append(list(map(int,input().split())))

for i in range(len(arr)-2,-1,-1):
    for j in range(i+1):
        arr[i][j]+=max(arr[i+1][j],arr[i+1][j+1])
print(arr[0][0])
#for i in range(n):
#    print(arr[i])
        
