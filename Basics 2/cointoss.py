import random

coin = ["head","tails"]
toss = random.choice(coin)

selection = input("head or tail")

if selection == toss:
    print("you win ! the coin landed on  ")

else:
    print("you loose! the coin landed on  " )
