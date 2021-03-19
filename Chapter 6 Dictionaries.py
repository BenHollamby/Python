#Dictionary what does it look like
alien_0 = {'colour': 'green', 'points': 5}
print(alien_0)
print(alien_0['colour'])
print(alien_0['points'])

#adding to a dictionary is as easy as 
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

#starting with an empty dictionary
alien_1 = {}

alien_1['colour'] = "black"
alien_1['points'] = 10

print(alien_1)

#print using keys
print(f"Alien Zero is the colour {alien_0['colour']}")
print(f"Alien One is the colour {alien_1['colour']}")

#changing values
alien_0 = {'colour': 'red', 'points': 5}
print(f"Alien Zero is now the colour {alien_0['colour']}")
alien_1 = {'colour': 'matte black'}
print(f"Alien One is now the colour {alien_1['colour']}")

#removing key-value pairs
del alien_0['points']
print(alien_0)

#using a dictionary to store many objects
fav_languages = {
    'alice': 'python',
    'sarah': 'c++',
    'ben': 'hcl',
    'will': 'powershell'
}

print(fav_languages)

person = {
    'first name': 'aaron',
    'last name': 'maisey',
    'age': 35,
    'city': 'hamilton'
}
print(person['first name'].title())
print(person['last name'].title())
print(person['age'])
print(person['city'].title())


#exercise asks to print name and fav number, lengthy, but it works, 
# but not very efficient use of code
fav_numbers = {
    'aaron': 30,
    'ben': 18,
    'alice': 25
}

print(f"Aaron's fav number is {fav_numbers['aaron']}")
print(f"Ben's fav number is {fav_numbers['ben']}")
print(f"Alice's fav number is {fav_numbers['alice']}")

print("\n")

#jumping ahead here, but the below is saying, for key, value in fav_numbers I 
# had to add on .items() This is because every item in a dict is a value 
# so using .items apparently stores it as a tuple. More learning needed
for key, value in fav_numbers.items():
    print(f"{key.title()}'s fav number is {value}")

#print values
print(fav_numbers.values())
#print keys
print(fav_numbers.keys())

#loopsing through dictionaries keys in a particlar order
for name in sorted(fav_numbers.keys()):
    print(name)


fav_languages_sec = {
    'alice': 'python',
    'sarah': 'powershell',
    'ben': 'python',
    'will': 'powershell'
}

#using set() to remove any duplicate values and only gives you unique items
for lang in set(fav_languages_sec.values()):
    print(lang)

#make a dictionary and write a sentence with the name and the country a river flows through
rivers = {
    'nile': 'egypt',
    'waikato': 'new zealand',
    'amazon': 'south america'
}

for key, value in rivers.items():
    print(f"\nThe {key.title()} river runs through the country {value.title()}.")

#make a list of people who should take a poll in fav language
#create another list of some who should
#loop through new list and if they have taken the poll print sorry
#if they havent taken the poll, ask them what their fav language is
third_fav_languages = {
    'alice': 'python',
    'sarah': 'c++',
    'ben': 'hcl',
    'will': 'powershell'
}

print("\n")

polls = ['alice', 'ben', 'rob', 'lemmy']
for poll in polls:
    if poll in third_fav_languages.keys():
        print(f"Sorry {poll.title()} you have already participated in the poll for a favourite language")
    else:
        print(f"What language do you prefer {poll.title()}?")
print("\n")

#create a list of dictionaries
alien_0 = {'colour': 'green', 'points': 5}
alien_1 = {'colour': 'red', 'points': 15}
alien_2 = {'colour': 'yellow', 'points': 10}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

#in this example we are going to create 30 aliens, show the first 5 and print the total number of aliens created
aliens = []

for alien_number in range(30):
    new_alien = {'colour': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

print(f"Total number of alients: {len(aliens)}")

print("\n")

#now imagine we want to change some characteristics of 3 aliens
#then printing first 5

for alien in aliens[:3]:
    if alien['colour'] == 'green':
        alien['colour'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

for alien in aliens[:5]:
    print(alien)

print("\n")

#we could extend this further by turning green to yellow and yellow to red

for alien in aliens[:6]:
    if alien['colour'] == 'green':
        alien['colour'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['colour'] == 'yellow':
        alien['colour'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

for alien in aliens[:10]:
    print(alien)


#create a list in a dictionary
#print order
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print(f"\nYou ordered a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

#another fun example
fav_languages_third = {
    'alice': ['python', 'go'],
    'sarah': ['powershell', 'python'],
    'ben': ['python', 'powershell', 'terraform'],
    'will': ['powershell', 'ruby']
}
for name, languages in fav_languages_third.items():
    print(f"\n{name.title()}'s favourite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

#dictionary in a dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")


#make 3 dictionaries about people, store in a list, then loop through people and list everything you know about them

person_1 = {
    'first name': 'aaron',
    'last name': 'maisey',
    'age': 35,
    'city': 'hamilton'
}

person_2 = {
    'first name': 'ben',
    'last name': 'hollamby',
    'age': 36,
    'city': 'sydney'
}

person_3 = {
    'first name': 'sam',
    'last name': 'millar',
    'age': 26,
    'city': 'auckland'
}

peoples = [person_1, person_2, person_3]
for person in peoples:
    name = person['first name'].title() + " " + person['last name'].title()
    age = str(person['age'])
    city = person['city'].title()

    print(name + ", of " + city + ", is " + age + " years old")

##################################################################################
print("\n")

animals_1 = {
    'type': "cat",
    'name': "fatshit",
}
animals_2 = {
    'type': "dog",
    'name': "jack",
}
animals_3 = {
    'type': "pig",
    'name': "piggy smalls",
}

pets = [animals_1, animals_2, animals_3]

for animal in pets:
    name = animal['name'].title()
    of_type = animal['type'].title()
    print(f"{name} is the coolest {of_type}")

################################################################

print("\n")

favourite_places = {
    'ben': ['antarctica', 'russia', 'siberia'],
    'aaron': ['australia', 'nz'],
    'alice': ['ireland', 'south america']
}

for name, places in favourite_places.items():
    print(f"{name.title()}'s favourite places are:")
    for place in places:
        print(f"\t{place.title()}")

##################################################

print("\n")

fav_numbers = {
    'aaron': [30, 45, 50],
    'ben': [18, 21, 25, 28],
    'alice': [25, 30, 33]
}

for name, numbers in fav_numbers.items():
    print(f"{name.title()}'s favourite numbers are:")
    for number in numbers:
        print(f"\t{number}")

