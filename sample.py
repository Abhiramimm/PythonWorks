# num=175

def is_disarium(num):
    num=str(num)
    digit_count=len(num)
    num =int(num)
    sum=0
    while(num!=0):
        digit=num%10
        exp=digit**digit_count
        sum=sum+exp
        num=num//10
        digit_count-=1
        if sum==num:
            return True
        else:
            return False
num = int(input("Enter a number to check if it's a Disarium number: "))
if is_disarium(num):
    print(num, "is a Disarium number.")
else:
    print(num, "is not a Disarium number.")
        
