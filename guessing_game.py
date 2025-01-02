#guessing game
secret_word = "hoes"
guess =""
number_of_tries = 0
guess_limit = 3
out_of_guesses = False

while guess!= secret_word and not(out_of_guesses):
    if number_of_tries < guess_limit:
        guess = input("Enter your guess: ")
        number_of_tries +=1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("You are out of guesses")
else:
    print("You win, Hooray!")
