from random import randint

print("Welcome to guess the random number game!")
print("Press enter to quit at any time")

random_number = randint(1,101)
count = 1
guesses = 0

while guesses != 5:

    guess = input("Guess a number between 0 - 100: ")
    if guess == '':
        break
    try:
        if int(guess) == random_number:
            print(f"Congratulations! You guess the number in {count} attempts! ")
            break
        elif int(guess) < random_number:
            print("Sorry, try a higher number!")
            count += 1
            guesses += 1
        elif int(guess) > random_number:
            print("Sorry, try a lower number!")
            count += 1
            guesses += 1
        
    except ValueError:
        print("Please enter a number!")

if guesses == 5:
    print(f"Sorry you ran out of tries! The number was {random_number}")