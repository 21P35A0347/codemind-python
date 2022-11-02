y = int(input())
x = list(map(int,input().split()))
n = len(str(max(x)))
b=[]
for i in x:
    b.append(len(str(i)))
print(b.count(n))