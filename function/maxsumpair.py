def maxpair(lst):
    largest=0
    sec_largest=0
    for num in lst:
        if num>largest:
            sec_largest=largest
            largest=num
    return largest,sec_largest

lst=[100,200,300,150]
print(maxpair(lst))