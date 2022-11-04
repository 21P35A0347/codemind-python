a,b=map(int,input().split())
s=0
m=[]
for i in range(a):
    l=list(map(int,input().split()))
    m.append(l)
for i in range(a):
    for j in range(b):
        if (i==0 or i==a-1) or (j==0 or j==b-1):
            s+=m[i][j]
print(s)