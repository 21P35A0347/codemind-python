x=int(input())
l=list(map(int,input().split()))
if x%2==0:
    print(*l)
else:
    print(*l,end=" ")
    print('0')