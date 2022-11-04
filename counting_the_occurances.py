x = input()
y = input()
s=0
for i in x:
    if i == y:
        s+=1
if s==0:
    print("-1")
else:
    print(s)