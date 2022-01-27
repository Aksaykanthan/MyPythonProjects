
from fractions import Fraction

a = []
n = int(input("Enter The Number of Digits "))
for i in range(n):
    a += list(map(Fraction,input("Enter the "+str(i+1)+" Number : ").rstrip().split()))
    add = sum(a)

print(add)
