import random
def shufflelist(lst):
    random.shuffle(lst)
    return lst
lst=[10,20,30,40]
print(shufflelist(lst))