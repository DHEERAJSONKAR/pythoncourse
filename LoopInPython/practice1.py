#. Sum up to n terms.

n = int(input("please enter the number:- "))
sum = 0
for i in range(1, n+1):
    sum = sum + i
print("the sum is:- ", sum)

# factorial of  number.
num = int(input("please enter the number:- "))
fact = 1
for i in range(1, num+1):
    fact = fact * i
print("the factorial is:- ", fact)


# print the sum of even or odd number in a range of separatly.
num = int(input("pleaase enter the number:- "))
even = 0
odd = 0
for i in range(1, num+1):
    if i%2 == 0:
        even = even +i
    else:
        odd = odd+i
print(f"the sum of even ande odd number is {even} and {odd}")

#. print all the factors of number.
n = int(input("which number you want to find the factors:- "))
for i in range(1, n+1):
    if n%i == 0:
        print(i)