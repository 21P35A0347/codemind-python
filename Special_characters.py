n=input()
l=[]
m=[]
nm="~!@#$%^&*()_+"
c=0
for i in n:
    if i.isdigit():
        if int(i)%2==0:
            l.append(i)
        else:
            m.append(i)
    if i in nm:
        c+=1
if len(m)>len(l):
    h=len(m)
else:
    h=len(l)
if c%2==0:
    i=0
    while True:
        if i==h:
            break
        if i<len(l):
            print(l[i],end="")
        if i<len(m):
            print(m[i],end="")
        i+=1
else:
    i=0
    while True:
        if i==h:
            break
        if i<len(m):
            print(m[i],end="")
        if i<len(l):
            print(l[i],end="")
        i+=1