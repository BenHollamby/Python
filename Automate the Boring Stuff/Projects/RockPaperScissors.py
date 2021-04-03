#first attempt at rock paper scissors
import random
import time

print("Welcome to 7 games of Rock, Paper, Scissors mother fucker!")
print("press enter anytime to quit")
print("press 'r' for Rock, 'p' for Paper, 's' for Scissors")

rock_paper_scissor = ['r', 'p', 's']

user_wins = 0
user_losses = 0
ties = 0
computer_wins = 0
computer_losses = 0

number_of_games = 0

computer_choice = random.choice(rock_paper_scissor)

while number_of_games != 7:
    computer_choice = random.choice(rock_paper_scissor)
    user_input = input("Please enter your choice: ")
    number_of_games += 1
    if user_input == '':
        break
    elif user_input == computer_choice:
        print("It's a tie!")
        ties += 1
    elif user_input == 'r' and computer_choice == 's':
        print("You win!")
        user_wins += 1
        computer_losses += 1
    elif user_input == 's' and computer_choice == 'r':
        print("You lose!")
        user_losses += 1
        computer_wins += 1
    elif user_input == 'p' and computer_choice == 'r':
        print("You win!")
        user_wins += 1
        computer_losses += 1
    elif user_input == 'p' and computer_choice == 's':
        print("You lose!")
        user_losses += 1
        computer_wins += 1
    elif user_input == 's' and computer_choice == 'p':
        print("You win!")
        user_wins += 1
        computer_losses += 1
    elif user_input == 'r' and computer_choice == 'p':
        print("You lose!")
        user_losses += 1
        computer_wins += 1

print(f"You won {user_wins} games, tied {ties} games and lost {user_losses} games!")

time.sleep(15)

