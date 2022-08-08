n = input()
l = list(map(int,input().split()))
k = int(input())
a = []
c = 0
for i in l:
    if l.count(i)==k:
        if i not in a:
            a.append(i)
            c+=1
if c==0:
    print(-1)
else:
    print(*a)