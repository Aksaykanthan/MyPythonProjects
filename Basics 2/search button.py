
find = input( "Find? ")

count = 1

line = "hello world"

for i in line:
    para = i.split()
    if find in para:
        print("Line Number ", count,":", i )

    count += 1

else:
    print("The Word Is Not Found. ")

