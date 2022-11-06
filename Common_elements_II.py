x,y=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in sorted(set(a),key=a.index):
    if i not in b:
        c.append(i)
for i in sorted(set(b),key=b.index):
    if i not in a:
        c.append(i)
print(*c)