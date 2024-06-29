def amstrong(lower,upper):
    sum=0
    for num in range(lower,upper+1):
        digit_count=len(str(num))
        num=int(num)
        original=num
        while(num!=0):
            digit=num%10
            exp=digit**digit_count
            sum+=exp
            num=num//10
        # return sum
    if original==sum:
        return sum
lower=int(input("enter lower limit:"))
upper=int(input("enter upper limit:"))
print(amstrong(lower,upper))


