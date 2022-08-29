#Queue
def isempty(l):
    if not l:
        return True
    return False

def enqueue(l,i):
    l.append(i)

def dequeue(l):
    if not isempty(l):
        l.pop(0)
    else:
        print('No Elements(UnderFlow)')

def peek(l):
    if not isempty(l):
        print(l[0])
    else:
        print('No Elements(UnderFlow)')
        

def display(l):
    if not isempty(l):
        for i in range(len(l)):
            print(f'{i} . {l[i]}')
    else:
        print('No Elements(UnderFlow)')

l = []
while True:
    print('1.Push\n2.Pop\n3.Peek\n4.Display\n5.Exit')
    ch = int(input('Option : '))
    if ch == 1:
        i = input('Element : ')
        enqueue(l,i)

    elif ch == 2:
        dequeue(l)
    
    elif ch == 3:
        peek(l)

    elif ch == 4:
        display(l)

    elif ch == 5:
        break
    
    else:
        print('Invalid Input')
