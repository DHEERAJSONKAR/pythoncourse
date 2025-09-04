# 1. Accept Two numbers and print the greastest between them.
num1 = int(input("Enter your First Number : "))
num2 = int(input("Enter your Second Number : "))
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    print("Both are equal number")


# 2. Accept the gender from the user as char and print the respective greeting message.
# Ex - good morning sir (on the basis of gender)
gen = input("please tell your gender as a character (M/F) : ")
if gen == 'M' or gen == 'm':
    print("Good Morning Sir")
elif gen == 'F' or gen == 'f':
    print("Good Morning Ma'am")
else:
    print("unidentify gender")


