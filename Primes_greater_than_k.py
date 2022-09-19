def is_prime(n):
    fc=0
    for i in range(1,n//2+1):
        if n%i==0:
            fc+=1
    if fc==1:
        return True
    else:
        return False
a=input()
l=list(map(int,input().split()))
k=int(input())
c=0
for i in l:
    if is_prime(i)==True and i>=k:
        c+=1
print(c)
        