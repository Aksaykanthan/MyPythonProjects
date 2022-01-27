
find = "hello"
para = "hello world"


count = 1

for i in para:
    words = para.split()
    if find.upper() in words:
        print("Line Number ", count,":", i )
        
    count += 1
    
else:
    print("The Word Is Not Found. ")
    

        
    
    
    
    


        
    
    


    