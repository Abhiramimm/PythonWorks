def twopairsum(arr):
    arr.sort()
    left=0
    right=len(arr)-1
    sum=8
    is_present=False

    while(left<right):
        r_element=arr[right]
        l_element=arr[left]
        current_sum=l_element+r_element
        if current_sum==sum:
            print(l_element,r_element)
            is_present=True
            break
        elif sum>current_sum:
            left+=1
        elif sum<current_sum:
            right-=1
    if is_present==False:
        print("no pairs")

arr=[2,3,5,4]
twopairsum(arr)