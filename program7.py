# find sum of square of n natural numbers
# (n=4 output= 1^2 + 2^2 + 3^2 + 4^2=30)

num=int(input("enter number:"))
sum=0

for num in range(1,num+1):
    square=num**2
    sum=sum+square
print(sum)

