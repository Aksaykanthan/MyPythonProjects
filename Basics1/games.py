
secret_word= input("Enter A Secret Word : ")
clue = input ("Enter a Clue (Optional) : ")

print("Don't Share to Your Friend "
      "You have 5 life to Guess the Correct one ")

guess = ""
guess_count = 0
guess_limit = 5
out_of_life = False

while guess != secret_word and not(out_of_life):

    if guess_count < guess_limit:
        guess = input("Enter guess : ")
        guess_count += 1

    else:
        out_of_life = True

if out_of_life:
    print("out of guesses")

else:
    print("you win!")

