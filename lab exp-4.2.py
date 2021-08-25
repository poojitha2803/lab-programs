4.2) Write a program that asks the user to enter two strings of the same length.
The program should then check to see if the strings are of the same length. If
they are not, the program should print an appropriate message and exit. If they
are of the same length, the program should alternate the characters of the two
strings. For example, if the user enters abcde and ABCDE the program should
print out AaBbCcDdEe

program:
s1=input("Enter any string:")
s2=input("Enyer another string:")
if (len(s1)!=len(s2)):
    print("Length of two stings are not same")
else:
    for i in range (0,len(s1)):
        print(s1[i]+s2[i],end="")
   
Output:
Enter any string:abcdef
Enyer another string:ABCDEF
aAbBcCdDeEfF    
