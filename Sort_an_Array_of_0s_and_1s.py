x = int(input())
l = list(map(int,input().split()))
m=[]
for i in l:
    if i==0:
        print(i,end=" ")
    else:
        m.append(i)
for j in m:
    print(j,end=" ")