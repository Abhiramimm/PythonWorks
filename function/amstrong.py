# num=175

def check_amstrong(num,digitcount):
    sum=0
    while(num!=0):
        digit=num%10
        sum=sum+digit**digitcount
        num=num//10
    if sum==org:
        return True
    else:
        return False
num = input("enter number: ")
digitcount=len(num)
num=int(num)
org=num
print(f"{num}",check_amstrong(num,digitcount))
        
