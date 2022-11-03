n=int(input())
m=input()
l=0
c=0
for i in m:
    if i=='1':
        c+=1
    elif i=='0':
        if l<c:
            l=c
            c=0
if l<c:
    print(c)
else:
    print(l)