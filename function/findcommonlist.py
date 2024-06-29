def commonlist(arr1,arr2):
    for num in arr2:
        if num in arr1:
            result=True
            break
    else:
        result=False
    return result

arr1=[1,2,3]
arr2=[3,4,5]
print(commonlist(arr1,arr2))












