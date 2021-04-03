#write a function that prints a sentence telling everyone what you are learning

def display_message():
    """ display message about what function be like """
    print("This chapter is all about functions!")

display_message()

#Write a function that accepts one parameter 'title', call the function and print a message

def favourite_book(title):
    print(f"{title.title()} is the best book!!")

favourite_book("malazan book of the fallen")

#you can set a default value in a function like so
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='willie')

print()

#write a function that accepts a size and some text for a message on a t-shirt then print a summary
def make_shirt(size, text):
    print(f"You have brought a {size} size shirt with the message '{text}' printed on it")

make_shirt('large', 'season in america be like')

#modify the shirt function so that shirts are large by default with a msg that reads i love python
def make_shirts(text, size='large'):
    print(f"You have brought a {size} shirt that reads {text.title()}")

make_shirts('i love python', 'small')
make_shirts('i love python')

print()

#write a function that accepts the name of a city and its country. Function should print a simple sentence
#give the parameter for the country a default value.
def describe_city(city, country='usa'):
    print(f"{city.title()} is in {country.title()}")

describe_city('los angeles')
describe_city('auckland', 'NZ')
describe_city('melbourne', 'australia')

print()
#example of Return Value
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
print()
#making an argument optional
def get_formatted_names(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()

musician = get_formatted_names('jimi', 'hendrix')
print(musician)
musician = get_formatted_names('john', 'hooker', 'lee')
print(musician)
print()

#returning a dictionary
def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

print()

#expanding on returning a dictionary | in conditional tests None equates to False
def build_persons(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_persons('jimi', 'hendrix', 27)
print(musician)

#Write a function that takes the name of a city and its country, return a string "city, country"

def city_country(city, country):
    return f"{city.title()}, {country.title()}"

place = city_country('auckland', 'new zealand')
print(place)
place = city_country('sydney', 'australia')
print(place)
place = city_country('vladivostok', 'russia')
print(place)
print()

#write a function that builds a dictionary describing a album.
#The function must take in an artist name and an album title
#use None to add an optional parameter to show the number of songs

def make_album(artist_name, artist_album, number_songs=None):
    album = {'name': artist_name, 'album': artist_album}
    if number_songs:
        album['tracks'] = number_songs
    return album

band = make_album('korn', 'life is peachy')
print(band)
band = make_album('nine inch nails', 'the downward spiral', 14)
print(band)

#write a while loop that allows users to enter an album's artist and title, make and print dictionary

def user_album(user_artist, album):
    record = {
        'name': user_artist,
        'album': album
        }
    return record

while True:
    request_artist = input("What is the name of the artist? \npress enter to quit\n")
    if request_artist == '':
        break
    request_album = input("What is the album? ")
    yo = user_album(request_artist, request_album)
    print(yo)
    
#make a list containing a series of short text messages, pass the list to a function
def show_messages(messages):
    for message in messages:
        print(message)
        print()

texts = ['ready to roll?', 'hey you up?', 'don\'t forget to study more yo']
show_messages(texts)
print()

#do the same as above but after printing each message move the message to a new list, prove it by printing both lists (This one I couldn't figure out why the last item would not move, turns out it stops )
unsent_messages = ['NIN all day', 'can\'t wait for Monday', 'study to break chains']
sent_messages = []
def sending_messages(texties):
    while unsent_messages:
        for i in texties:
            sender = unsent_messages.pop()
            print(sender)
            sent_messages.append(sender)

sending_messages(unsent_messages)
print(unsent_messages)
print(sent_messages)
print()

#do the same but have an archived version of the messages

messages_to_send = ['NIN all day', 'can\'t wait for Monday', 'study to break chains']
messages_to_archive = []

def archiving_messages(text_messages):
    messages_to_copy = [messages_to_send[:]]
    while messages_to_copy:
        for message in messages_to_copy:
            sending = messages_to_copy.pop()
            messages_to_archive.append(sending)

archiving_messages(messages_to_send)
print(messages_to_send)
print(messages_to_archive)
print()

#write a function that accepts a list of items a person wants on a sandwich, and have one parameter that will accept as many items as the functions calls
# print a summary of the order as well
def sandwiches(bread, *condiments):
    print(f"You have selected a {bread.title()} sandwich:")
    for condi in condiments:
        print(f"\t{condi}")


sandwiches('white', 'cheese', 'ham', 'pickle')
print()
sandwiches('rye', 'ham')
print()
sandwiches('italian herbs and cheese', 'ham', 'salami', 'cheese', 'red onion', 'lettuce', 'honey mustard sauce')

#create a user profile function that takes first and last name as arguments, and three other key-value pairs
def user_profile(first, last, **info):
    info['first_name'] = first
    info['last_name'] = last
    print(info)

user_profile('ben', 'holl')
user_profile('ben', 'holla', location='Hamilton', age=26, salary='large')

#write a function that stores information about a car
def make_car(manufacturer, model, **carinfo):
    carinfo['manufacturer'] = manufacturer
    carinfo['model'] = model
    return carinfo

car = make_car('subaru', 'legacy', color='blue', tow_package=True)
print(car)

