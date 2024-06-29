def hcf(num1,num2):
    i=1
    hcf=1
    small=num1 if num1<num2 else num2
    while(i<=small):
        if(num1%i==0) and(num2%i==0):
            hcf=i
        i+=1
    return hcf
print(hcf(4,6))