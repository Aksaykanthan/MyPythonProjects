
class area():
    def square(l):
        a =  l**2 
        return a
    def reactangle(l,b):
        a = l * b
        return a
    def triangle(b,h):
        a = (b*h)/2
        return a 

class perimeter():
    def square(l):
        p = 4*l
        return p
    def reactangle(l,b):
        p = 2(l+b)
        return p
    def triangle(b,h,l):
        p = l + b + h
        return p 
    def shape():
        p = 0
        n = int(input("Enter the number of side their in the shape ? "))
        for i in range(n):
            l = int(input("Enter the length of the number of side : "))
            p += l
        return p
        