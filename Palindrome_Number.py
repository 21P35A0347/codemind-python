x = int(input())
for i in range(x):
    n = int(input())
    m = n
    s = 0
    while n!=0:
        v = n%10
        s = s*10+v
        n = n//10
        if m==s:
            print("True")
            break
        
    else:
        print("False")