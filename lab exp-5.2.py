5.2) Write a program that asks the user for an integer and creates a list that
consists of the factors of that integer.

Program:
n=int(input("Enter any number:"))
s=[]
for i in range(1,n+1):
    if(n%i==0):
        s.append(i)
print(s)        

Output:
Enter any number:24
[1, 2, 3, 4, 6, 8, 12, 24]    
