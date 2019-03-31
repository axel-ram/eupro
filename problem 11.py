arr = [list(map(int, input().split())) for i in range(20)]
maxr=0
maxd=0
maxdia=0
ans=0
imax=0
jmax=0
for i in range(17):
    for j in range(17):
        maxr = arr[i][j]*arr[i][j+1]*arr[i][j+2]*arr[i][j+3]
        maxd = arr[i][j]*arr[i+1][j]*arr[i+2][j]*arr[i+3][j]
        maxdia = arr[i][j]*arr[i+1][j+1]*arr[i+2][j+2]*arr[i+3][j+3]
        if i+3>=3:
            maxudia=arr[i][j+3]*arr[i+1][j+2]*arr[i+2][j+1]*arr[i+3][j]
            diff=max(maxr,maxd,maxdia,maxudia)
        else:
            diff=max(maxr,maxd,maxdia)
        if diff>ans:
            ans=diff
print(ans)
