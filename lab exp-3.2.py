3.2) Generate a random number between 1 and 10. Ask the user to guess the
number and print a message based on whether they get it right or not.

Program:
import random
r=random.randint(1,10)
guess=int(input("Enter your guess number:"))
if (r==guess):
    print("Your guess is correct")
else:
    print("Your guess is wrong")

Output:
Enter your guess number:3
Your guess is wrong

Enter your guess number:5
Your guess is wrong
