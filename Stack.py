#Stack
def isempty(l):
    if not l:
        return True
    return False

def push(l,i):
    l.append(i)

def Pop(l):
    if not isempty(l):
        l.pop()
    else:
        print('No Elements(UnderFlow)')

def peek(l):
    if not isempty(l):
        print(l[-1])
    else:
        print('No Elements(UnderFlow)')    

def display(l):
    for x in range(len(l)-1,-1,-1):
        print(f'{x} . {l[x]}')
    else:
        print('No Elements(UnderFlow)')

l = []
while True:
    print('1.Push\n2.Pop\n3.Display\n4.Exit')
    ch = int(input('Option : '))
    if ch == 1:
        i = input('Element : ')
        push(l,i)

    elif ch == 2:
        Pop(l)

    elif ch == 3:
        peek(l)

    elif ch == 4:
        display(l)

    elif ch == 5:
        break
    
    else:
        print('Invalid Input')
