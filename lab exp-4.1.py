4. Strings
4.1) Write a program that asks the user to enter a word and prints out whether
that word contains any vowels.

Program:
word=input("Enter any word")
for i in word:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        print("Word contain vowels")
        break
else:
    print("Word doesnot contain vowels")

Output:
Enter any wordaditya
Word contain vowels    
