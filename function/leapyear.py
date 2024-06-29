def leap(yr):
    
    if (yr%100==0 and yr%400==0)or (yr%100!=0 and yr%4==0):
        return f"{yr} is leap year"
    else:
        return f"{yr} is not a leap year"

yr=int(input("enter yr:")) 
print(leap(yr))