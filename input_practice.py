from random import randint

def guess_game(a,b):
    correct = randint(a,b)
    guess_number = None
    while guess_number != correct:
        guess = input(' --> ')
        try:
            guess_number = int(guess)
        except ValueError:
            print("Please enter an integer between {} and {}".format(a,b))
            continue
        if guess_number < correct:
            print("too low")
        elif guess_number > correct:
            print("too high")
    print("You did it :)")


guess_game(1, 99)


