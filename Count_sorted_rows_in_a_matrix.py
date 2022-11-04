a,b=map(int,input().split())
s=0
m=[]
for i in range(a):
    l=list(map(int,input().split()))
    m.append(l)
for i in m:
    n=i
    c=sorted(i)
    i=sorted(i,reverse=True)
    if n==i or n==c:
        s+=1
print(s)