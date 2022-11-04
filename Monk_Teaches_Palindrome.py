x = int(input())
for i in range(x):
    n = input()
    a = n[::-1]
    if n==a:
        if len(n)%2==0:
            print('YES EVEN')
        else:
            print('YES ODD')
    else:
        print('NO')