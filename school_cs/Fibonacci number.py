n = 20
f = [0,1]
for k in range(n):
    for i in f:
        a = f[-1]+f[-2]
        f.append(a)
        break
print(f)
