x = int(input())
l = list(map(int,input().split()))
c,d=0,0
for i in range(x):
    if i%2==0 and l[i]%2==0:
        c+=1
    if l[i]%2==0:
        d+=1
if c==d:
    print(True)
else:
    print(False)