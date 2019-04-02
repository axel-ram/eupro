#I know I should find solution without using simple mathematics but python supports big numbers :P
num=2**1000
sum=0
n=num
while(n>0):
    sum+=n%10
    n=n//10
print(num)
print(sum)
#Will find solution (algorithm) that can run on any language
