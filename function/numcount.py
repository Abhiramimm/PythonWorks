def numcount(lst):
    new_lst=[]
    wc={num:lst.count(num) for num in set(lst)}
    return wc
            

lst=[1,0,1,0,1,0,1]
print(numcount(lst))