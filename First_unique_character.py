z = input().lower()
s=0
for i in z:
    if i>='a' and i<='z':
        if z.count(i)==1:
            s=1
            print(i)
            break
if s==0:
    print('-1')