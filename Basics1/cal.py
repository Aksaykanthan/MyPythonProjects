a = int(input("a : "))
b = int(input("b : "))
o = input("o: ")

add = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
div = lambda a, b: a / b

if o == "+":
    print(add(a, b))
elif o == "-":
    print(sub(a, b))
elif o == "*":
    print(mul(a, b))
elif o == "/":
    print(div(a, b))
else:
    print("Only + - * / are allowed")
