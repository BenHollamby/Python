cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#run the two below in actual python shell
car = 'bmw'
car == 'bmw'

#prints True
racer = "audi"
print("\n")
print(racer == 'audi')

#prints false as compare statement has a capital
racer = "audi"
print("\n")
print(racer == 'Audi')

#prints true because variable has title appended
racer = "audi"
print("\n")
print(racer.title() == 'Audi')

#prints true because it does not equal Audi
racer = "audi"
print("\n")
print(racer != 'Audi')


alien_color = 'green'

if alien_color == 'green':
    print(True)

alien_color = 'yellow'

if alien_color == 'green':
    print(True)

print("\n")

alien_color = 'green'

if alien_color == 'green':
    print("5 points!")

if alien_color != 'green':
    print("10 points!")

if alien_color == 'green':
    print("5 points!")
else:
    print("10 points!")



alien_color = 'green'
if alien_color == 'green':
    print("\n5 points!")
elif alien_color == 'yellow':
    print("\n10 points!")
else:
    print("\n15 points!")

alien_color = 'yellow'
if alien_color == 'green':
    print("\n5 points!")
elif alien_color == 'yellow':
    print("\n10 points!")
else:
    print("\n15 points!")

alien_color = 'red'
if alien_color == 'green':
    print("\n5 points!")
elif alien_color == 'yellow':
    print("\n10 points!")
else:
    print("\n15 points!")


age = 30
if age < 2:
    print("\nPerson is a baby")
elif age >= 2 and age < 4:
    print("\nPerson is a toddler")
elif age >= 4 and age < 13:
    print("\nPerson is a kid")
elif age >= 13 and age < 20:
    print("\nPerson is a teenager")
elif age >= 20 and age < 65:
    print("\nPerson is an adult")
elif age >= 65:
    print("\nPerson is an elder")


favourite_fruits = ["banana", "apple", "onion"]

for fruit in favourite_fruits:
    if fruit == "apple":
        print(f"you must like {fruit.title()}'s")

if 'banana' == favourite_fruits[1]:
    print(True)

if 'banana' == favourite_fruits[0]:
    print(True)


usernames = ["admin", "angela", "alice", "kelly", "elisha", "natalie"]

for user in usernames:
    if user == 'admin':
        print(f"\nHello {user.title()}, would you like to see a status report?")
    else:
        print(f"Hello {user.title()} thanks for logging in again.")


#When the name of a list is used in an if statement, Python returns True if the
# list contains at least one item; an empty list evaluates to False.
no_users = []
if no_users:
    for no_user in no_users:
        print("Hello")
else:
    print("we need some users!")

#loop through new_users and if the name has already been used, reject because the name has been taken
current_users = ["admin", "angela", "alice", "kelly", "elisha", "natalie"]
new_users = ["angela", "alice", "kelly", "ben"]

for new_user in new_users:
    if new_user in current_users:
        print(f"\nSorry {new_user.title()} you will need a new username")
    else:
        print(f"\nFeel free to join {new_user.title()}")

#make sure list is case sensitive if Kelly has been used, KELLY should not be accepted
#using a list comprehension for current users turning all users into lower case
current_users = ["admin", "angela", "alice", "Kelly", "elisha", "natalie"]
new_users = ["angela", "alice", "KELLY", "ben"]

lower_users = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in lower_users:
        print(f"\nSorry no dice {new_user.title()} ")
    else:
        print(f"\nWelcome to the fold {new_user.title()}")

#ordinal numbers indicate position in a list, most end in th, except for 1st 2nd and 3rd
numbers = list(range(1,10))
for number in numbers:
    if number == 1:
        print(f"\n{number}st!")
    elif number == 2:
        print(f"{number}nd.")
    elif number == 3:
        print(f"{number}rd.")
    else:
        print(f"{number}th")

