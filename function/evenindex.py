def evenindex(text):
    even_lst=[]
    for i in text:
        if text.index(i)%2==0:
            even_lst.append(i)
    return even_lst

print(evenindex("python"))

