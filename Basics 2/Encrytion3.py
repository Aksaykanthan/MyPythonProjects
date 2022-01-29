
def encrypt(m):
    global lk, r, l
    l = [ord(i) for i in m]
    lk = max(l)
    li = 127 - max(l)
    import random
    r = random.randint(1, li)
    n = ''
    for i in m:
        k = ord(i)
        k += r
        n += chr(k)
    n += str(r)
    n += '|' if len(str(r)) == 2 else ''
    return n


def decrypt(m):
    global t, u
    n = ''
    t = m[-3]+m[-2] if m[-1] == '|' else m[-1]
    for i in m:
        k = ord(i)
        k -= int(t)
        n += chr(k)
    u = [i for i in n]
    if m[-1] == '|':
        u.pop(-1)
        u.pop(-2)
        u.pop(-3)
        u.pop(-4)
    else:
        u.pop(-1)

    return ''.join([str(i) for i in u])


m = 'aksay'

for o in range(100):
    s = 'w' if o == 1 else 'a'
    y = encrypt(m)
    b = decrypt(y)
    f = open('Wrong.txt', s)
    c = open('Correct.txt', s)
    e = open('error.txt', 'a')
    k = open('error.txt', 'r')
    if b == m:
        c.write(f'{b}  --->   {y}  random code = {r}  max word = {lk} t = {t} \n')
    if b != m:
        f.write(
            f'{b}  --->   {y}  random code = {r}  max word = {lk} t = {t} u = {u} \n')
        if m not in k.read():
            e.write(f'{m} \n')
f.close()
c.close()
k.close()
e.close()
