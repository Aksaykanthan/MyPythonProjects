# Write a function in Python to swap() first half of the elements with the second half of the elements. Also implement this function in a Python Program
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def swap(l):
    return l[len(l)//2:] + l[:len(l)//2]


print(swap(l))

# Write a recursive function in Python to find the factorial of a natural number. Also implement this function in a Python Program.


def factorial(l):
    k = 1
    for i in range(1, l+1):
        k *= i
    return k


print(factorial(6))

# Write a recursive function in python to find out the sum of digits of any integer number. Also implement this function in a Python program


def sum_digits(n):
    k = 0
    for i in str(n):
        k += int(i)
    return k


print(sum_digits(123456))

# Write a recursive function to compute the nth Fibonacci number. Also implement this function in a Python Program


def fn(n):
    l = [0, 1]
    for i in range(1, n):
        l.append(l[-1]+l[-2])
    return l[-1]


print(fn(10))

# Write a recursive function in Python to find the sum of all elements of a list. Also implement this function in a Python Program


def sum_list(l):
    sum = 0
    for i in l:
        sum += i
    return sum


print(sum_list(l))

# Write a recursive Python program to test if a string is a palindrome or not.


def palindrone(str):
    return 'it is a palindrone' if str == str[::-1] else 'it is not a palindrone'


print(palindrone('mom'))

# Write a Python Program to read a text file. Find out the total number of words available in this file.


def count_words(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return len(data.split())


print(count_words('test.txt'))

# Write a program in Python to read a text file line by line and print it on the screen.


def read_file(filename):
    with open(filename, 'r') as f:
        data = f.read()
        print(data)

# Write a program in python to read a text file and remove all the lines that contain the character `a’ in a file and write it to another file.


def remove_words(filename, word='a'):
    with open(filename, 'r') as f:
        data = f.read()
    k = list(data)
    d = ''
    for i in k:
        if word != i:
            d += i
    with open('test1.txt', 'w') as f:
        f.write(d)
# remove_words('test.txt')

# Write a Python program to implement a stack using a list data-structure.


def write(list):
    str = input('Write: ')
    list.append(str)


def read(list):
    for x, y in enumerate(list):
        print(x, '=>', y)


def delete(list):
    str = int(input('Which one do you want to delete ?  '))
    read(list)
    list.pop(str)


def main():
    l = []
    while True:
        print('1.Write\n2.Read\n3.Delete')
        op = int(input('Op :'))
        if op == 1:
            write(l)
        elif op == 2:
            read(l)
        elif op == 3:
            delete(l)
# main()


def prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False


l = [7, 4, 5, 8, 9, 6, 1, 23, 4]
k = []
for i in l:
    if prime(i):
        k.append(i)
print(k)
