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


third_fav_languages = {
    'alice': 'python',
    'sarah': 'c++',
    'ben': 'hcl',
    'will': 'powershell'
}

poll = ['alice', 'ben', 'rob', 'lemmy']
for third in third_fav_languages.keys():
    print(third)

#page 164