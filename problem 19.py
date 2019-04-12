#We can do this problem with calendar library which I found in the solutions of online blogs .
#But I wanted a solution without using a library implemented by someone else.

count=0
year=1901
flag=0
x=1
while(year<=2000):
    if year%100==0 and year%400==0:
        flag=1
    else:
        if year%100!=0 and year%4==0:
            flag=1
        else:
            flag=0
    #print(year,flag)
    for month in range(1,13):
        if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
            x+=3
        elif month==2:
            x+=flag   
        else:
            x+=2
        if x%7==6:
            count+=1
        x=x%7
    year+=1
print(count)
            
