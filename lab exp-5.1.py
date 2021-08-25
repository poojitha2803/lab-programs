5. Data structure
5.1) Write a program that generates a list of 20 random numbers between 1 and
100.
(a) Print the list.
(b) Print the average of the elements in the list.
(c) Print the largest and smallest values in the list.
(d) Print the second largest and second smallest entries in the list
(e) Print how many even numbers are in the list.

Program:
import random
a=[]
for j in range(20):
    a.append(random.randint(1,100))
print("list:",a)
print("Average of elements in the list:",sum(a)/len(a))
print("Largest of the list:",max(a))
print("smallest of the list:",min(a))
a.sort()
print("Second Largest of the list:",a[-2])
print("Second smallest of the list:",a[1])
count=0
for i in range (0,len(a)):
    if(a[i]%2==0):
        count+=1
print("Even numbers:",count)        

Output:
list: [52, 14, 16, 8, 3, 2, 23, 62, 84, 2, 70, 76, 67, 56, 91, 12, 73, 51, 52, 21]
Average of elements in the list: 41.75
Largest of the list: 91
smallest of the list: 2
Second Largest of the list: 84
Second smallest of the list: 2
Even numbers: 13    
