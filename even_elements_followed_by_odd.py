n = input()
l = list(map(int,input().split())) 
c = []
for i in l:
    if i%2==0:
        c.append(i)
for i in l:
    if i%2==1:
        c.append(i)
print(*c)