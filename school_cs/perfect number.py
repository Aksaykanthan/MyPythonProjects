
def prefect(num):
    t=0
    for i in range(1, num):
        if (num % i) == 0:
            t+=i
        
    if t == num:
        print("it is a prefect number")
    else:
        print("no")

prefect(5)

