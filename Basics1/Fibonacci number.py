
#Fibonacci series

def Fibonacci_number(n):
    num1 = 0
    num2 = 1
    if n == 0:
        print(num1)
    else:
        print(num1)
        print(num2)
    for Fibonacci_number in range(n):
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        print(num3)
Fibonacci_number(int(input("How many numbers you want in this series? :  ")))
