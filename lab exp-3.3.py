3.3) Write a program that asks the user for two numbers and prints Close if the
numbers are within .001 of each other and Not close otherwise.

Program:
a=float(input("Enter first number:"))
b=float(input("Enter second number:"))
if abs(a-b)<=0.001:
    print("Close")
else:
    print("Not close")

Output:
Enter first number:3.456
Enter second number:3.457
Close

Enter first number:3.6789
Enter second number:4.5678
Not close    
