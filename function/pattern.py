def pattern():
    for row in range(1,6):
        for col in range(1,4):
            print("*",end="\t")
        print()
pattern()

def pattern(rowstart,rowstop,colstart,colstop):
    for row in range(rowstart,rowstop):
        for col in range(colstart,colstop):
            print("*",end="\t")
        print()
pattern(1,6,1,4)