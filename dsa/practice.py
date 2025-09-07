#. print positive and negative element of an list.
# l = [12,3,-4,5,-6,-7,8,-9]
# print("positive element are: ")
# for i in l:
#     if i>=0:
#        print(i)
# print("negative element are: ")
# for i in l:
#     if i<0:
#         print(i)

#. mean of list element.
# li = [1,2,3,4,5]
# sum = 0
# for i in li:
#     sum = sum + i
#     mean = sum/len(li)
# print(f"mean of list element is: {mean}")

# 3. find the greatest element and print its index too.
# a = [234,456,342,454,345,456,543]
# largest = a[0]
# index = 0
# for i in range(len(a)):
#     if a[i]>largest:
#         largest = a[i]
#         index = i
# print(f"the largest element is: {largest}")
# print(f"the index of largest element is: {index}")

#. find the second largest number.
# list = [12,13,45,67,89,23,45,67]
# largest = list[0]
# second_lar=list[0]
# for i in list:
#     if i>largest:
#         second_lar = largest
#         largest = i
#     elif i>second_lar:
#         second_lar = i
# print(f"the second largest number is: {second_lar}")
# print(f"the largest number is: {largest}")

#. check if list is sorted or not.
a=[12,13,14,15,16]
for i in range(len(a)-1):
    if a[i]<a[i+1]:
        continue
    else:
        print("list is not sorted")
        break
else:
    print("list is sorted")

