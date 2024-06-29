def reversedigit(num):
    result=""
    while(num!=0):
        digit=num%10
        result+=str(digit)
        num=num//10
    return result
print(reversedigit(123))