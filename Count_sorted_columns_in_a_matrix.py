a,b=map(int,input().split())
s=0
m=[]
for i in range(a):
    l=list(map(int,input().split()))
    m.append(l)
i=0
while i!=b:
    v=[]
    for j in m:
        v.append(j[i])
    dupli=v
    so_v=sorted(v)
    v=sorted(v,reverse=True)
    if dupli==v or so_v==dupli:
        s+=1
    i+=1
print(s)