y = int(input())
for j in range(y):
    x = input()
    c=0
    for i in x:
        if i.isdigit():
            c=1
    if c==1:
        print('Yes')
    else:
        print('No')