word=input("Enter any word")
for i in word:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        print("Word contain vowels")
        break
else:
    print("Word doesnot contain vowels")
