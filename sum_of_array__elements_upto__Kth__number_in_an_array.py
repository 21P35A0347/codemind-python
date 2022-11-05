x=int(input())
l=list(map(int,input().split()))
k=int(input())
s=0
for i in l:
    if i==k:
        break
    s+=i
print(s+k)