def calculator(num1,num2,operator):
    
    if operator=="+":
        result=num1+num2
        return result
    elif operator=="-":
        result=num1-num2
        return result
num1=int(input("enter num1"))
num2=int(input("enter num2")) 
operator=input("enter operator")   
print(calculator(num1,num2,operator))