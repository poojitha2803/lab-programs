3. Control Flow Continued
3.1) Use a for loop to print a triangle like the one below. Allow the user to
specify how high the triangle should be.
*
**
***
****

Program:
n=int(input("Enter the value of n:"))
for i in range (0,n):
    for j in range (0,i):
        print("*",end=" ")
    print( )

Output:
Enter the value of n:5
* 
* * 
* * * 
* * * *     
