4.4) In algebraic expressions, the symbol for multiplication is often left out, as
in 3x+4y or 3(x+5). Computers prefer those expressions to include the
multiplication symbol, like 3*x+4*y or 3*(x+5). Write a program that asks the
user for an algebraic expression and then inserts multiplication symbols where
appropriate.

Program:
exp = input("Enter algebric expression: ")
cexp = ''
for ch in exp:
    if ch>='0' and ch<='9':
        cexp = cexp + ch
    elif ch=='(':
        cexp = cexp + '*' + ch
    elif ch>='a' and ch<='z' and cexp[-1]!='(':
        cexp = cexp + '*' + ch
    else:
        cexp = cexp + ch
print("Converted expression is :",cexp)

Output:
Enter algebric expression: 3x+4y
Converted expression is : 3*x+4*y    
