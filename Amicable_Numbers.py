x = int(input())
y = int(input())
a,b=0,0
for i in range(1,x):
    if x%i==0:
        a+=i
for i in range(1,y):
    if y%i==0:
        b+=i
if a==y and b==x:
    print('Amicable')
else:
    print('Not Amicable')