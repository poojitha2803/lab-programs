import random
r=random.randint(1,10)
guess=int(input("Enter your guess number:"))
if (r==guess):
    print("Your guess is correct")
else:
    print("Your guess is wrong")
