def pattern(n):
    for row in range(1,n+1):
        for col in range(1,row+1):
            print("*",end=" ")
        print()
    for row in range(n-1,-1,-1):
        for col in range(1,row+1):
            print("*",end=" ")
        print()
pattern(5)