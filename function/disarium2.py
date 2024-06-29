def is_amstrong(num):
    sum=0
    digit_count=len(num)
    num=int(num)
    org=num
    while(num!=0):
        digit=num%10
        exp=digit**digit_count
        sum+=exp
        num=num//10
        digit_count-=1
    if sum==org:
        return True
    else:
        return False

num=input("enter number:")
print(is_amstrong(num))
