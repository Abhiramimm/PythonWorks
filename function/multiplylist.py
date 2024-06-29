def multiplylist(lst):
    new_lst=[]
    for i in lst:
        new_lst.append(i**2)
    return new_lst
lst=[1,2,3,4]
print(multiplylist(lst))