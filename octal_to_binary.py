n = int(input())
i=0
s=0
while n!=0:
    v = n%10
    s+=v*(8**i)
    n=n//10
    i+=1
print("{0:b}".format(s))