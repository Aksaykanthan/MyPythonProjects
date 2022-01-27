

print("Students Details")

try:
    #name
    name = str(input("Enter Your Name : "))
    while len(name) > 20:
        print("Invalid Max input is 20 char")
        if len(name) > 20:
            name = input("Enter Your Name : ")

    #class
    Class = int(input("Enter Your Class : "))
    while Class > 12 :
        print("Invalid Max input is 12 Num")
        if Class > 12 :
            Class = int(input("Enter Your Class : "))

    #subjects
    subject = []
    global sub
    sub = int(input("How Many Subjects Do You Have : "))
    for n in range(sub):
        numbers = int(input("Enter the Marks Of The "+str(n+1)+" Subject : "))
        while numbers > 100:
            print("Invalid Max input is 100 Num")
            if numbers > 100:
                numbers = int(input("Enter the Marks Of The "+str(n+1)+" Subject : "))
        subject.append(numbers)

    #to add
    def total():
        global add
        add = sum(subject)
        print("Your Total Mark Is ", str(add) , "Out Of ",str(sub*100))

    # average
    def average():
        global av
        av = add/sub
        print("Your Average Marks Is ", str(av) + "!" )

    #pass or fail
    def passorfail():
        if av >= 35:
            print("Congratulations! You Are Pass!")
        else:
            print("You Are Fail")

    #printing answers
    print("Name = " , name )
    print("Class = " , Class )
    total()
    average()
    passorfail()

except ValueError:
    print("Invalid Input Try Again ! ")
