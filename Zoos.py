x = input()
d = 0
c = 0
for i in x:
    if i=='z':
        d+=1
    else:
        c+=1
if 2*d==c:
    print("Yes")
else:
    print("No")