n=input()
l=[]
for i in n:
    if i>='a' and i<='z':
        l.append(i)
    elif i>='A' and i<='Z':
        l.append(i)
l=l[::-1]
i=0
for j in n:
    if j in l:
        print(l[i],end="")
        i+=1
    else:
        print(j,end="")