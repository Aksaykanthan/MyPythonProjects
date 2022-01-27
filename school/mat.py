
class math():
    
    a = float
    b = float
    
    def add(a,b):
        ans = a + b  
        print(f'Addition Of {a} and {b} is {ans}')
        
    def sub(a,b):
        ans = a - b  
        print(f'Subraction Of {a} and {b} is {ans}')
        
    def mul(a,b):
        ans = a * b  
        print(f'Multification Of {a} and {b} is {ans}')

    def div(a,b):
        ans = a / b 
        print(f'Divition Of {a} and {b} is {ans}')
            
    def sqr(a,b):
        ansa = a**2 
        ansb = b**2 
        print(f'Square Of {a} is {ansa}')
        print(f'Square Of {b} is {ansb}')
        
    def is_greater(a,b):
        if a > b :
            print(f"{a}is Greater than {b}")
        elif a < b :
            print(f"{b}is Greater than {a}")
        else :
            print(f"{a} and {b} are equal")

    def odd_even(a,b):
        if a % 2 == 0:
            print(f"{a} is A Even Number")
        else:
            print(f"{a} Is A Odd Number")
            
        if b % 2 == 0:
            print(f"{b} is A Even Number")
        else:
            print(f"{b} Is A Odd Number")
            
    def prime(a):
        if a > 1:
            for i in range(2, a ):
                if (a % i) == 0:
                    print(a, "is not a prime number")
                    print("Because",i, "times", a // i, "is", a )
                    break
            else:
                print(a, "is a prime number")
        else:
            print(a, "is not a prime number")
            
        
    
class text():
    
    def find(word ,para):
        if word.upper() in para.upper():
            print("Yes")
        else:
            print("No")
            
    
