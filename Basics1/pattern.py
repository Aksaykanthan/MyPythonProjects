m = 40

a = [i for i in range(1,m+1)]

for i in range(len(a)):
    for i in a:
        print(i,end = ' ')
    print()
    a.pop()


