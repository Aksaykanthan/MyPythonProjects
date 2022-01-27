from random import randint

heads = 0
tails = 0

flip = int(input("how many times do u want the coin to toss ?  "))

for i in range(flip):
    result = random.randint(0, 1)

    if result == 0:
        heads += 1
    else :
        tails += 1

#print("the probality of getting heads and tails are " + heads + "/" + tails )




