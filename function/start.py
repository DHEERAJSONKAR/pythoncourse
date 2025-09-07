def hello():
    print("this is a syntax of basic function")
hello() #. this is called default argument

def sum(a,b):
    print(f"the sum of {a} and {b} is {a+b}")
sum(10,23)   #. this is called positional argument

def hy(name, age):
    print(f"my name is {name} and age is {age}")
hy(age=23, name ="Dheeraj")   #. this is Called keyword argument

def pallindrome(st):
    rev = ""
    for i in range(len(st)-1,-1,-1):

        rev = rev + st[i]
    if rev == st:
        print(f"{st} is pallindrome")
    else:
        print(f"{st} is not pallindrome")
pallindrome("madam")
pallindrome("dheeraj")