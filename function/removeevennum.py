def RemoveEvenNum(lst):
    for i in lst:
        if i%2==0:
            lst.remove(i)
    return lst

lst=[1,2,3,4,5]
print(RemoveEvenNum(lst))