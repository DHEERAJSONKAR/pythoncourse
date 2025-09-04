# 3. Accept an integer and check whether it is even number or odd number.
num = int(input("Enter your number: "))
if num%2 == 0:
    print(f"{num} is even number")
else:
    print(f"{num} is a odd number.")

# 4. Accept name and age from user. check if the user is valid voter or not.
name = input("please tell me your name : - ")
age = int(input("tell me your age : -  "))
if age>=18:
    print(f"Hello {name} you are a valid voter")
else:
    print(f"hello {name} you are not a valid voter")

# 5. Accept a years and check if it is a leap year or not.
year = int(input("Enter a year : -  "))
if year%100==0 and year%400==0:
    print(f"{year} is a leap year")
elif year%100!=0 and year%4 ==0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year.")