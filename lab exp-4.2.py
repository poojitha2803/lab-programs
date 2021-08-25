s1=input("Enter any string:")
s2=input("Enyer another string:")
if (len(s1)!=len(s2)):
    print("Length of two stings are not same")
else:
    for i in range (0,len(s1)):
        print(s1[i]+s2[i],end="")
   
