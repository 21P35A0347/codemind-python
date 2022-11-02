l = int(input())
for i in range(int(input())):
    w , h = map(int,input().split())
    if w<l or h<l:
        print('UPLOAD ANOTHER')
    elif l<=w and l<=h:
        if w==h:
            print('ACCEPTED')
        else:
            print('CROP IT')