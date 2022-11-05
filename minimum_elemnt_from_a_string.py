x = list(map(str,input().split()))
x = x[len(x)-1]
n = min(x)
m=n
if n.isupper():
    if n.lower() in x:
        print(n.lower())
    else:
        print(n)
else:
    print(n)