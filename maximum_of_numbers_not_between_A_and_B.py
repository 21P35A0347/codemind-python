n = input()
l = list(map(int,input().split()))
a,b = map(int,input().split())
c = []
x = 0
for i in l:
    if i<a or i>b:
        x+=1
        c.append(i)
if x==0:
    print(-1)
else:
    print(max(c))