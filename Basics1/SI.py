
print("Simple Interest Calculator")

principal = int(input("Enter The Principal Amount : "))
interest = int(input("Enter The Rate Of Interest : "))
time = int(input("Enter The Time : "))

def SI():
    si = principal*interest*time
    print(si)

SI()


