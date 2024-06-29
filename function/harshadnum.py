def is_harshad(num):
    sum=0
    original=num
    while(num!=0):
        digit=num%10
        sum+=digit
        num=num//10
        print(num)
    if original%sum==0:
        return True
    else:
        return False
    
num=int(input("enter number:"))
print(is_harshad(num))
