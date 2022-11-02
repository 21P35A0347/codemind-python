def palin(n):
    a=n
    s=0
    if n<0:
        n=n*-1
    while n!=0:
        i = n%10
        s = s*10+i
        n = n//10
    if a==s:
        return 1
    else:
        return 0
x = int(input())
l = list(map(int,input().split()))
c=0
for i in l:
    if palin(i):
        c+=1
print(c)