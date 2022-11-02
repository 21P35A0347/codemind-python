x = int(input())
m=1
s=0
while x!=0:
    v = x%10
    x = x//10
    s+=v
    m*=v
print(m-s)