a,b=map(int,input().split())
l=[]
m=[]
for i in range(a):
    v=list(map(int,input().split()))
    m.append(v)
i=0
while i!=b:
    s=0
    for j in m:
        s+=j[i]
    l.append(s)
    i+=1
print(*l)