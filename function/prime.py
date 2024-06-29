def prime(num):
    is_prime=True
    if num==1:
        is_prime=False
    else:
        for i in range(2,num):
            if num%i==0:
                is_prime=False
    return is_prime
num=int(input("enter num:"))
print(prime(num))