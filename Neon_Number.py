x = int(input())
n = x**2
s=0
while n!=0:
    v = n%10
    n = n//10
    s+=v
if s==x:
    print("Neon Number")
else:
    print("Not Neon Number")