def rotate_list(lst):
    for i in range(0,2):
        last_element=lst.pop()
        lst.insert(0,last_element)
    return lst

lst=[1,2,3,4,5,6,7]
print(rotate_list(lst))