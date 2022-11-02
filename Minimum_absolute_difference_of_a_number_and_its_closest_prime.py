def is_prime(i):
    c=0
    for ii in range(2,i):
        if i%ii==0:
            c+=1
    if c==0:
        return i


x = int(input())
f = x
for i in range(x,2,-1):
    if is_prime(i):
        n = i
        break
while f!=0:
    if is_prime(f):
        m = f
        break
    f+=1
n = x-n
m = m-x
if is_prime(x):
    print('0')
elif n<m:
    print(n)
else:
    print(m)