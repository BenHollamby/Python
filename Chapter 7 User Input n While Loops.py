#ask for input and stored as a variable
car = input("What kind of rental car are you after sir/maam? ")
print(f"Let me see if I can find you a {car.title()}")

#ask how many people are coming for dinner, if more than 8 they will have to wait
#else their table is ready | You need to convert input string to an interget with int(variable)
dinner_seats = input("How many people are coming for dinner? ")
if int(dinner_seats) > 8:
    print("Sorry you will have to wait a bit longer")
else:
    print(f"Your table for {dinner_seats} is ready")

#module % is super handy, divides one number by another and returns the remainder
#using | if number % 2 == 0 | if it is true, number is even. if not true the number is odd.
#ask for a number and report back whether the number is a multiple of 10.

number = input("What is the number to check? ")
if int(number) % 10 == 0:
    print(f"{number} is a multiple of 10!")
else:
    print(f"{number} is not a multiple of 10.")

print()

#using the while loop
current_number = 0
while current_number < 5:
    print(current_number)
    current_number += 1
print(f"Total of current number is {current_number}\n")

#letting the user choose when to quit
prompt = "\nTell me something and I will repeat it back to you:"
prompt += "\Enter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

#another way of doing the above is using a True flag
prompt = "\nTell me something and I will repeat it back to you:"
prompt += "\Enter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

#using break to exit a loop
prompt = "\nPlease enter the name of a city you have visited:\n"
prompt += "\Enter 'quit' to end the program. "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"\nI'd love to go to {city.title()}!")

#if you don't want to break out of a loop but move to the next piece of code you
#can use the continue statement to return to the beginning of the loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

#write a loop that prompts the user for the topping they would like on their pizza
#and keep asking until quit is entered
prompt = "What topping would you like on your pizza? \n Enter 'quit' to finish: "
topping = ""
while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"\nAdding {topping} to your pizza!\n")

################################################################
prompt = int(input("Please enter your age: "))

while True:
    if prompt < 3:
        print(f"You are under {prompt} years of age, ticket is free!")
        break
    elif prompt >= 3 and prompt <= 12:
        print(f"Because you are aged {prompt} the cost of your ticket is $10")
        break
    elif prompt > 12:
        print(f"You are {prompt} years of age, cost is $15")
        break

########################################################################
prompt = "What topping would you like on your pizza? \n Enter 'quit' to finish: "
topping = ""
active = True
while active:
    topping = input(prompt)
    if topping == 'quit':
        active = False
    else:
        print(f"\nAdding {topping} to your pizza!\n")

#moving items from one list to another
#a for loop is effective for looping through a list, but if you are going to modify a list
# a while loop is much more efficient
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#removing all instances of a specific value in a list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

#filling a dictionary with User Input
responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response

    repeat = input("keep going yes/no? ")
    if repeat == 'no':
        polling_active = False
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}.")

# Make a list called sandwich_orders and fill it with the names of various sandwiches.
#Then make an empty list called finished_sandwiches. Loop through the list of sandwich
#orders and print a message for each order, such as I made your tuna sandwich. As each
#sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been
#made, print a message listing each sandwich that was made.
sandwich_orders = ['ham n cheese', 'toasted cheese', 'double cheese']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Making a {current_sandwich.title()} now.")
    finished_sandwiches.append(current_sandwich)

for finished in finished_sandwiches:
    print(f"A {finished.title()} sandwich was made to order.")

#add code to explain pastrami has run out and remove all occurances from list.
sandwich_orders = ['pastrami', 'ham n cheese', 'toasted cheese', 'pastrami', 'double cheese', 'pastrami']
finished_sandwiches = []

print("We apologize, but we have run out of pastrami due to Covid-19")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Making a {current_sandwich.title()} now.")
    finished_sandwiches.append(current_sandwich)

for finished in finished_sandwiches:
    print(f"A {finished.title()} sandwich was made to order.")


#write a program that polls users about their dream vacation, store in a dictionary and the publish the results
vacations = {}

while True:
    name = input("\nWhat is your name? (press enter to quit) ")
    if name == "":
        break
    vacation = input("And where would you like to go?")
    vacations[name] = vacation

print()

for key, value in vacations.items():
    print(f"{key.title()} would love to visit {value.title()}")