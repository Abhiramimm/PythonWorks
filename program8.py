# program to find common elements from 2 list

list1=[10,20,30,40]
list2=[30,40,50,60]

# for num1 in list1:
#     for num2 in list2:
#         if num1==num2:
#             print(num1)

for i in range(0,len(list1)+1):
    for j in range(0,len(list2)+1):
        if list1[i]==list2[j]:
            print(list1[i])
    