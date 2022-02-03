
def lr(m):
    h = {x: 0 for x in m}
    l = r = 0

    for i in m:
        if h[i] == 0:
            lc = i-1
            rc = i+1

        while lc in h:
            h[lc] = 1
            lc -= 1
        lc += 1

        while rc in h:
            h[rc] = 1
            rc += 1
        rc -= 1

        if (r-l) <= (rc-lc):
            r = rc
            l = lc

    return [l, r]


m = [1, 2, 3, 4]
print(lr(m))
