def even(start,stop):
    for i in range(start,stop+1):
        if i%2==0:
            print(i)
            i+=1
even(1,10)