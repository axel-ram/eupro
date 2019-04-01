#python supports big numbers so there is no need to hustle to add big numbers :P
sum=0
for i in range(100):
    sum+=int(input())
print(sum)
l=len(str(sum))
print(sum//(10**(l-10)))
