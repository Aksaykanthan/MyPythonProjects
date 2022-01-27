try :
    num1 = float(input("enter the number : "))
    num2 = float(input("enter the number : "))

    def add():
        result = num1 + num2
        print("The Sum of " + str(num1) +" and " + str(num2) +" is " + str(result))

    def sub():
        result = num1 - num2
        print("The Sub of " + str(num1) + " and " + str(num2) + " is " + str(result))

    def mul():
        result = num1 * num2
        print("The Multiplication of " + str(num1) + " and " + str(num2) + " is " + str(result))

    def div():
        result = num1 / num2
        print("The Division of " + str(num1) + " and " + str(num2) + " is " + str(result))

    op = (input("enter the operation : "))
    if op == "+":
        add()
    elif op == "-":
        sub()
    elif op == "*":
        mul()
    elif op == "/":
        div()
    else:
        print("Invaild")
    
except ValueError:
    print("Only Numbers Are Allowed")

except ZeroDivisionError:
    print("Denominator cannot be 0 ")

