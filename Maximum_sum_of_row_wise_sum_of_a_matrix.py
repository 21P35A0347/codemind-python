a,b=map(int,input().split())
m=[]
n=[]
l=[]
for i in range(a):
    u=list(map(int,input().split()))
    m.append(u)
for i in range(a):
    s=0
    for j in range(b):
        s+=m[i][j]
    l.append(s)
print(max(l))