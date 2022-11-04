n=input()
c=1
d=1
a="aeiouAEIOU"
for i in range(1,len(n)):
    if n[i-1] in a and n[i] in a:
        c+=1
    else:
        if c>d:
            d=c
            c=0
if c>d:
    print(c)
else:
    print(d)