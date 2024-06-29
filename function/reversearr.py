# def arr_reverse(arr):
#     result=arr.reverse
#     return result
# arr=[10,20,30,40]
# print(arr_reverse(arr))

def reversearr(arr):
    new_arr=[]
    for i in range(len(arr)-1,-1,-1):
        new_arr.append(arr[i])
    return new_arr
arr=[1,2,3,4]
print(reversearr(arr))



# def arr_reverse(arr):
#      return arr.reverse()
# arr=[10,20,30,40]
# print(arr_reverse(arr))