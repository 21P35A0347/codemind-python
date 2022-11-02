x = input()
a = int(x)**2
y = x[::-1]
b = int(y)**2
c = str(b)
d = c[::-1]
if str(a)==d:
    print(True)
else:
    print(False)