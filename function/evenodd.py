def evenodd(string):
    even=[]
    odd=[]
    for i in string:
        if string.index(i)%2==0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd
even,odd=evenodd("hello")
print("even:",even)
print("odd:",odd)