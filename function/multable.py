def multable(num):
    mul=1
    for i in range(1,11):
        mul=i*num
        print(f"{i} * {num} = {mul}")
multable(8)