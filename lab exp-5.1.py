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
