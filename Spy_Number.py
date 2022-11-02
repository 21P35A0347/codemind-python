x = eval(input())
s=0
p=1
while x!=0:
    m = x%10
    x=x//10
    s+=m
    p*=m
if s==p:
    print("Spy Number")
else:
    print("Not Spy Number")