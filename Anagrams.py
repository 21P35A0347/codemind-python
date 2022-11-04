a=input().lower()
b=input().lower()
c=0
for i in a:
    if i in b:
        c+=1
if c==len(a):
    print(True)
else:
    print(False)