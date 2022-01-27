
a, b, c = 5, 5, 5

if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
elif c > b and c > a:
    print(c)
elif a == b == c:
    print(a, b, c, sep=" = ")
