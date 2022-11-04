x = list(map(str,input().split()))
res=''
for i in x:
    for j in i:
        res = j + res
    print(res,end=" ")
    res=''