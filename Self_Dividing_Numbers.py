x=int(input())
y=int(input())
for i in range(x,y+1):
    a=str(i)
    k=len(str(i))
    c=0
    for j in a:
        if int(j)!=0 and int(a)%int(j)==0:
            c+=1
    if c==k:
        print(a,end=" ")
