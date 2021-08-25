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
