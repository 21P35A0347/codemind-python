x = int(input())
l = list(map(int,input().split()))
k=[]
c=0
for i in list(set(l)):
    if l.count(i)==i:
        k.append(i)
if k == []:
    print('-1')
else:
    print(format(sum(k)/len(k),".2f"))