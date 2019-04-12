#MADE AN ARRAY THAT STORES EACH DIGIT OF THE MULTIPLICATION RESULT
arr=[0 for i in range(400)]
carry=0
count=0
arr[0]=1
print(arr[0])
for i in range(2,101):
    for j in range(400):
        temp =arr[j]*i
        arr[j]=(temp+carry)%10
        carry=(temp+carry)//10
#print(arr)
sum=0
for i in range(400):
    sum+=arr[i]
print(sum)
