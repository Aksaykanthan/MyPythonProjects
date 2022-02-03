from random import uniform


def pi(n):
    c = 0
    t = 0
    for _ in range(n):
        x = uniform(0, 1)
        y = uniform(0, 1)
        dist = x**2 + y**2
        if dist <= 1:
            c += 1
        t += 1
    return 4*(c/t)


print(pi(100000000))
