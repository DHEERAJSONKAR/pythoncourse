#. accept a number and check if a perfect number or not.
# a number whose some of factors is equal to the number itself. ex- 6=1,2,3 = 6
# n = int(input("check your number is perfect or not:- "))
# sum = 0
# for i in range(1,n):
#     if n%i == 0:
#         sum = sum + i
# if sum == n:
#     print("this number is perfect number.")
# else:
#     print("this number is not a perfect number.")

#. check whether a number is prime or not.
# n = int(input("check your number is prime or not:- "))
# count = 0
# for i in range(1, n+1):
#     if n%i == 0:
#         count = count + 1
# if count == 2:
#     print("this number is prime number.")
# else:
#     print("this number is not prime number.")

#. reverse a string without using in build functions.
# string = input("please enter a string:- ")
# rev =""
# for i in range(len(string)-1,-1,-1):
#     rev = rev + string[i]
# print(f"the reverse string is:- {rev}")

#. check string is palindrone or not.
# x = input("check a number or string is palindrone or not:- ")
# y = ""
# for i in range(len(x)-1,-1,-1):
#     y = y + x[i]
# if x==y:
#     print(f"{x} is palindrone ")
# else:
#     print(f"{x} is not palindrone ")


#. count all letter, digit and special symbol from a given string.
'''string
given: str1 = "P@#yn26at^&i5ve"
expected outcome:
total counts of chars, digit, and symbols
chars = 8
digit = 3
symbol = 4'''

a = "sdfgdgedxgd1234@#$%U"
char = 0
dig = 0
spchr =0
for i in a:
    if i.isdigit():
        dig = dig +1
    elif i.isalpha():
        char = char +1
    else:
        spchr = spchr + 1
print(f"your digit are {dig}\n your alphabets are {char}\n your special char {spchr}")  

