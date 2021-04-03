#make a guess the number game
#brought to you by Massive Attack Mezzanine

from random import randint

print("Welcome to guess the random number game!")
print("Press enter to quit at any time")

random_number = randint(1,21)
count = 1

while True:

    guess = input("Guess a number between 1 - 20: ")
    if guess == '':
        break
    try:
        if int(guess) == random_number:
            print(f"Congratulations! You guess the number in {count} attempts! ")
            break
        else:
            print("Sorry keep trying!")
            count += 1
    except ValueError:
        print("Please enter a number!")