    while 'P.T' in sub1[3:] or 'P.T' in sub1[0]  or "Maths" in sub1[3:]:
            shuffle(sub1)
        if sub[j] == sub1[j]:
            shuffle(sub1)
        sub1.insert(4,"Lunch")        
        print("",item +" " * (9-len(item)),*sub1,"",sep="  |  ")
        print("-"*115)
        sub1.remove("Lunch")
        shuffle(sub1)
 