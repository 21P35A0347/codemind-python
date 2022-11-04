a,b=map(int,input().split())
c=[]
m=[]
for i in range(a):
    l=list(map(int,input().split()))
    m.append(l)
i=0
while i!=b:
    s=0
    for j in m:
        s+=j[i]
    c.append(s)
    i+=1
print(max(c))