def evensum(num):
    sum=0
    for i in range(0,num+1):
        if i%2==0:
            sum+=i
    return sum
print(evensum(20))
    