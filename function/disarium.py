def check_disarium(num,digitcount):
    sum=0
    while(num!=0):
        digit=num%10
        exp=digit**digitcount
        sum+=exp
        num=num//10
        digitcount-=1
    if sum==org:
        return True
    else:
        return False
num=input("enter number:")
digitcount=len(str(num))
num=int(num)
org=num
print(f"{num} is disarium  number:",check_disarium(num,digitcount))