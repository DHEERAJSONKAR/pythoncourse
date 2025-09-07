# 1. write a python script to merge to python dictionaries.
# d1 = {1:10, 2:20, 3:30, 4:40}
# d2 = {5:50, 6:60, 7:70}
# for i in d2:
#     d1[i] = d2[i]
# print(d1)

# 2. write a python program to sum all the value in a dictionary.
# d = {1:10, 2:20, 3:30, 4:40}
# sum = 0
# for i in d:
#     sum = sum + d[i]
# print("sum of the all dictionary value is: ",sum)

# 3. count the frequency of each element in a list.
# a = [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,4,5,4,5,4,5]
# d= {}
# for i in a:
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)

# 4. write a python program to combine two dictionary by values for common keys.
d1 = {1:10, 2:20, 3:30, 4:40}
d2 = {4:30,5:50, 6:60, 7:70}
for i in d2:
    if i in d1.keys():
        d1[i] += d2[i]
    else:
        d1[i] = d2[i]
print(d1)
