n=input()
lst=list(map(int,input().split()))
s=[]
for i in lst:
    if i not in s:
        s.append(i)
a=sorted(s)
if a==lst:
    print("yes")
else:
    print("no")