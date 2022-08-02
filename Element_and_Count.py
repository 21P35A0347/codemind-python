n=input()
l=list(map(int,input().split()))
c=[]
m=0
for i in l:
    if i not in c:
        m=l.count(i)
        print(i,m, end=" ")
        c.append(i)