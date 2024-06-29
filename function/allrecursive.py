def allrecursive(text):
    recursive_lst=[]
    wc={ch:text.count(ch) for ch in set(text)}
    for k,v in wc.items():
        if v>1:
            recursive_lst.append(k)
    return recursive_lst
print(allrecursive("goodmorning"))