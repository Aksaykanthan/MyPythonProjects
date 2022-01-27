
def powers(bnum,pnum):
    result = 1
    for index in range(pnum):
        result= result * bnum
    return result


print(powers(5,2))
