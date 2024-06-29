def commonelement(lst):
    wc={ch:lst.count(ch) for ch in set(lst)}
    for k,v in wc.items():
        if v>1:
            return k
lst=[2,2,3,4,4]
print(commonelement(lst))