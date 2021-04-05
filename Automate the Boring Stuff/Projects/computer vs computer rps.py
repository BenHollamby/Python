#second attempt computer vs computer rock paper scissors
#100 million games takes about a minute. Good fun!
import random

print()
print("Welcome to computer vs computer of Rock, Paper, Scissors mother fucker!")
print("Battle commencing.....")

rock_paper_scissor = ['r', 'p', 's']

computer1_wins = 0
computer1_losses = 0

ties = 0

computer2_wins = 0
computer2_losses = 0

number_of_games = 0

while number_of_games != 100000000:

    computer_choice1 = random.choice(rock_paper_scissor)
    computer_choice2 = random.choice(rock_paper_scissor)
    number_of_games += 1

    if computer_choice1 == computer_choice2:
        ties += 1

    elif computer_choice1 == 'r' and computer_choice2 == 's':
        computer1_wins += 1
        computer2_losses += 1

    elif computer_choice1 == 's' and computer_choice2 == 'r':
        computer1_losses += 1
        computer2_wins += 1

    elif computer_choice1 == 'p' and computer_choice2 == 'r':
        computer1_wins += 1
        computer2_losses += 1

    elif computer_choice1 == 'p' and computer_choice2 == 's':
        computer1_losses += 1
        computer2_wins += 1

    elif computer_choice1 == 's' and computer_choice2 == 'p':
        computer1_wins += 1
        computer2_losses += 1

    elif computer_choice1 == 'r' and computer_choice2 == 'p':
        computer1_losses += 1
        computer2_wins += 1

print(f"There were {number_of_games} games played!")

print(f"{ties} of those were tied games!")

print(f"Computer 1 won {computer1_wins} games,and lost {computer1_losses} games!")

print(f"Computer 2 won {computer2_wins} games and lost {computer2_losses} games!")

if computer1_wins == computer2_wins:
    print(f"The result is a tie after {number_of_games}!")

elif computer1_wins > computer2_wins:
    comp1_by = (computer1_wins - computer2_wins)
    print(f"Computer 1 is the overall winner with {computer1_wins} to {computer2_wins} winning by {comp1_by} match points!")

else:
    comp2_by = (computer2_wins - computer1_wins)
    print(f"Computer 2 is the winner with {computer2_wins} to {computer1_wins} winning by {comp2_by} match points!")
