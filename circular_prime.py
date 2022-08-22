def is_prime(n):
    fc = 0
    for i in range(1,n//2+1):
        if n%i==0:
            fc+=1
    if fc==1:
        return True
    else:
        return False
def rev(n):
    r=0
    while n>0:
        b = n%10
        r = r*10+b
        n = n//10
    return r
n = int(input())
r = rev(n)
if is_prime(n)==True and is_prime(r)==True:
    print("circular prime")
elif is_prime(n)==True and is_prime(r)==False:
    print("prime but not a circular prime")
elif is_prime(n)==False:
    print("not prime")