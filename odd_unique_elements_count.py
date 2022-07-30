n=input()
l=list(map(int,input().split()))
a=[]
count = 0
for i in range(len(l)):
    if l[i] not in a:
        a.append(l[i])
for j in range(len(a)):
    if a[j]%2==1:
        count+=1
print(count)