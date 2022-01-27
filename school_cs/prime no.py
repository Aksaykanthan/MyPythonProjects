try:
    num = int(input('Enter A Number To Check Whether It Is A PrimeNumber Or Not : '))

    def prime():
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    print(num, "is not a prime number")
                    print("Because",i, "times", num // i, "is", num)
                    break
            else:
                print(num, "is a prime number")
        else:
            print(num, "is not a prime number")

    def eo():
        if (num % 2) == 0:
            print(num , "is Even number")
        else:
            print(num , "is Odd number")

    prime(),eo()

except ValueError:
    print('Only Numbers Are allowed')

