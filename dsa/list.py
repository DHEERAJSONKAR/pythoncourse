a = [12,3,42,34,5.6,"hello",True]
#. 1st way using index
for i in range(len(a)):
    print(a[i])

#. 2nd way using directly on values
for i in a:
    print(i)



l = [1,2,3,4]
l.append(5)
l.append(8)
l.insert(5,6,)
l.insert(6,7)
print(l)

b = [45,5,756,674]
b[1]= 100
print(b)
b.remove(756)
print(b)
b.pop(2)
print(b)