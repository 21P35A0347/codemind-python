x = list(map(str,input().lower().split()))
s=0
for i in x:
    n = i[::-1]
    if i==n:
        s+=1
print(s)