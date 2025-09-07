# 1. seprate each digit of a number and at print it a new line.
# a = int(input("enter the number: "))
# while a>0:
#     print(a%10)
#     a = a// 10

# 2. Accept a number and print its reverse.
# num = int(input("enter the number: "))
# rev = 0
# while num>0:
#     rev = rev*10 + num%10
#     num = num // 10
# print("the reverse number is: ", rev)

# 3. Accept a number and check if it is a palindromic number(if number at its reverse are qequal)
# a = int(input("enter the number: "))
# copy = a
# rev = 0
# while a>0:
#     rev = rev*10 + a%10
#     a = a//10
# if copy == rev:
#     print(f"{copy} is a palindromic number.")
# else:
#     print(f"{copy} is not a palindromic number.")

# 4. create a random number guessing game with python.
import random
num = random.randint(1,10)
tries = 0
while True:
    guess = int(input("guess a number between 1 to 10: "))
    tries += 1
    if num == guess:
        print(f"you are right you guessed the number is {tries} tries.")
        break
    elif num <guess:
        print("go to little lower")
        
    elif num > guess:
        print("go to little higher")
        
    else:
        
        print("sorry you lost the game.")
