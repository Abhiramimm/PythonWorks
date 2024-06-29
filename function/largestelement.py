def largestelement(arr):
    largest=arr[0]
    for i in range(0,len(arr)):
        if arr[i]>largest:
            largest=arr[i]
    return largest

arr=[2,3,4,5,6]
print(largestelement(arr))