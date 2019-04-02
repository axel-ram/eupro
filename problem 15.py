
n=20
grid=[[0 for i in range(n+1)] for j in range(n+1)]

#for x in range(n+1):
#    print(grid[x])
for i in range(n+1):
    grid[i][n]=1
    grid[n][i]=1

for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):
        #print(i,j)
        grid[i][j]=grid[i+1][j]+grid[i][j+1]

for x in range(n+1):
    print(grid[x])
print(grid[0][0])

"""
Solution I found online was a less memory consuming
print ("Hello, world!")
import math
n=20
path=math.factorial(2*n)//math.factorial(n)**2
print(path)
"""
