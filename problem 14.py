n=1000000
#to keep track of already visited numbers less than currently visiting number
counts=[0 for i in range(n+1)]
maxlength=0
maxnumber=0
counts[1]=1

for i in range(2,n+1):
    number=i
    length=0
    #counting the no. of terms
    while(number!=1 and number>=i):
        if number%2==0:
            number//=2
        else:
            number=(3*number+1)
        length+=1
    #updating the value of current number with the help of already visited number
    counts[i]=length+counts[number]
    
    if counts[i]>maxlength:
        maxnumber=i
        maxlength=counts[i]
print(maxnumber,maxlength)
    
    
