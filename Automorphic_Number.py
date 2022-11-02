x = input()
a = len(x)
y = str(int(x)**2)
b = len(y)
s=''
for i in range(b-a,b,1):
    s+=y[i]
if x==s:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')