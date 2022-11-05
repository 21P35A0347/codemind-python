x = int(input())
l = list(map(int,input().split()))
if x%2==0:
    for i in range(x//2):
        print(l[i],end=" ")
        print(l[x-1-i],end=" ")
else:
    for i in range(x//2+1):
        if i!=(x-i-1):
            print(l[i],end=" ")
            print(l[x-1-i],end=" ")
    print(l[i],end=" ")
    print('0')