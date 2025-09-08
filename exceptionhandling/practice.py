# a = int(input("enter the number: "))
# try:
#     print(10/a)
# except Exception as err:
#     print("division by zero is not possible")
# else:
#     print("good there is no exception.")
# finally:
#     print("I will execute anyway.")
# print("hello")

age = int(input("enter your age: "))
try:
   if age<10 or age>18:
    raise ValueError("age is not valid")
   else:
     print("welcome to the class")
except Exception as err:
    print(f"error is {err}")
print("thank for giveing oppurtunity.")