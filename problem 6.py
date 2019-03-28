n=int(input())
sumOfSquares=int((n*(n+1)*(2*n+1)/6))
squareOfSums=int((n*(n+1)/2)**2)
difference=squareOfSums - sumOfSquares
print(difference)
