def fib(n,x,a,b):
    if n<x:
        c = a + b
        a , b = b , c
        print(b,end=" ")
        fib(n+1,x,a,b)

x = int(input())
a,b = 0,1
print(a,end=" ")
print(b,end=" ")
fib(1,x-1,a,b)