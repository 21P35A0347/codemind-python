def reverse(n):
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
a=input()
lst=list(map(int,input().split()))
s=[]
for i in lst:
    if(i>0 or i not in s):
        a=reverse(i)
        s.append(a)
print(*s)