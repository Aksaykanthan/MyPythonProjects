
def amstrong(x):
    x = str(x)
    r = 0
    for i in x:
        i = int(i)
        r+= i*i*i
        
    if r == int(x):
        print("yes")
    else:
        print("no")

amstrong(153)

