from random import shuffle

sub = ["Maths",
       "Physics",
       "English",
       "P.T",
       "Computer Science",
       "Chemistry",
       "Biology"]

sub1 = [
    "Maths",
    "Physics",
    "English",
    "P.T",
    "Computer Science",
    "Chemistry",
    "Biology",]

d = ["monday",
     "tuesday",
     "wednesday",
     "thursday",
     "friday",
     "saturday"]

print("  |    Days     |")
print("-" * 115)

is_same = lambda sub,sub1: False if sub == sub1 else shuffle(sub1) 

for item in d:
    while "P.T" in sub[3:] or "P.T" in sub[0] or "Maths" in sub[3:]:
        shuffle(sub)
    sub.insert(4, "Lunch")
    print("", item + " " * (9 - len(item)), *sub, "", sep="  |  ")
    print("-" * 115)
    sub.remove("Lunch")
    shuffle(sub)

for item in d:
    while "P.T" in sub1[3:] or "P.T" in sub1[0] or "Maths" in sub1[3:] :
        shuffle(sub1)
    sub1.insert(4, "Lunch")
    print("", item + " " * (9 - len(item)), *sub1, "", sep="  |  ")
    print("-" * 115)
    sub1.remove("Lunch")
    shuffle(sub1)