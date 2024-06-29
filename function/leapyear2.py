def leap(yr):

    if (yr%100==0 and yr%400==0)or (yr%100!=0 and yr%4==0):
       print("leap yr")
    else:
       print("not leap yr") 
yr=int(input("enter yr:"))
leap(yr)