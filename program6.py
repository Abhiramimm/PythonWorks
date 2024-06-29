# program to find frequency of elements in a list
# (eg: element1 : count, element2: count....)

lst=[10,20,10,30,20,10,40]
wc={}
for num in lst:
    if num in wc:
        wc[num]+=1
    else:
        wc[num]=1
print(wc)

lst1=["red","green","blue","red","white"]
wc={l:lst1.count(l) for l in lst1}
# print(wc)