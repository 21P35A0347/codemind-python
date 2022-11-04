x = input()
c=0
for i in range(len(x)):
    for j in range(len(x)):
        if x[i]==x[j]:
            c+=1
    if c==1:
        print(i)
        break
    c=0
else:
    print('-1')