x=int(input())
l=list(map(int,input().split()))
m=[]
k=[]
for i in set(l):
    m.append([l.count(i),i])
p=max(m)[0]
for i in m:
    if i[0]==p:
        k.append(i[1])
print(min(k))