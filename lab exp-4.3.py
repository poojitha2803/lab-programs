4.3) Write a program that asks the user for a large integer and inserts commas
into it according to the standard American convention for commas in large
numbers. For instance, if the user enters 1000000, the output should be
1,000,000.

Program:
n=int(input("Enter a number:"))
print("The number seperated with commas is:{:,}".format(n))

Output:
Enter a number:10000000
The number seperated with commas is:10,000,000  
