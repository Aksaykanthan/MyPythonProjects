
try:
    number = float(input("Enter A Number : "))
    print(number)

except ZeroDivisionError:
    print("ZeroDivisionError")

except ValueError:
    print("invalid input(text), Only Intgers are applicable")
