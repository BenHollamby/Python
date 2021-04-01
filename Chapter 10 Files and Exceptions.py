#this is how to open a file in current directory and print to screen
with open('py_digits.txt') as file_object: #opens text file and saves all info in file_object
    contents = file_object.read() #save content to variable
print(contents) #notice the extra line, can be removed with .rstrip()

#Learning Python: Open a blank file in your text editor and write a few lines
#summarizing what you’ve learned about Python so far. Start each line with the phrase In Python
#you can. . .. Save the file as learning_python.txt in the same directory as your exercises from this
#chapter. Write a program that reads the file and prints what you wrote three times. Print the
#contents once by reading in the entire file, once by looping over the file object, and once by
#storing the lines in a list and then working with them outside the with block.
filename = 'broken.txt'
print("--- Reading in the entire file:")
with open(filename) as f:
    contents = f.read()
print(contents)

print("\n--- Looping over the lines:")
with open(filename) as f:
    for line in f:
        print(line.rstrip())

print("\n--- Storing the lines in a list:")
with open(filename) as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip())

print()

#you can replace() method any word in a string with a different word like so
message = "I really like dogs"
print(message)
print(message.replace('dogs', 'cats'))

#writing to an empty file
filename = 'programming.txt'

with open(filename, 'w') as file_object: # 'w' will overwrite anything, using 'a' will append
    file_object.write('I love Python, fo sho ')
    file_object.write('you know its true') #this stays on the first line cause no sep
    file_object.write("\nCant take my eyes offa\n") #new lines
    file_object.write("\tyou")

#Guest: Write a program that prompts the user for their name. When they respond, write
#their name to a file called guest.txt.
filename = 'tendashthree.txt'
persons_name = input("What is your name? ")
with open(filename, 'w') as file_object:
    file_object.write(f"Hello {persons_name.title()}!")


#Guest Book: Write a while loop that prompts users for their name. When they enter
#their name, print a greeting to the screen and add a line recording their visit in a file called
#guest_book.txt. Make sure each entry appears on a new line in the file.

filename = 'tendashfour.txt'

while True:
    name = input("Hello, what is your name?")
    if name == '':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(f"Hello {name.title()}, looking well yo!\n")

#10-5. Programming Poll: Write a while loop that asks people why they like programming.
#Each time someone enters a reason, add their reason to a file that stores all the responses.
filename = 'programming.txt'

while True:
    programming_poll = input("Why do you like programming? ")
    if programming_poll == '':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(f"{programming_poll.upper()} caps for emphasis! \n")


#handling exceptions use a try: and then grab the error with except
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

#using exceptions to prevent crashes
print("give me two numbers and I'll divide them.")
print("press enter to quit")


#a proper example of handling the exception, the mistake I made here was putting Try at the start and except at the end
#what i needed to do what put it round the bit that would actually fail, in this case the answer and throwing in an else block
while True:
    first_number = input("\nFirst number: ")
    if first_number == '':
        break
    second_number = input("Second number: ")
    if second_number == '':
        break
    try:    
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("Can't be done my friend, can't divide by zero just ain't goan happen. Try again :) ")
    else:
        print(answer)

#handline the FileNotFoundError Exception
#Lets start with an error 
#filename = "alice.txt"
#with open(filename, encoding='utf-8') as f:
#    contents = f.read()

#now we add some error handling
filename = "alice.txt"
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry the {filename} does not exist")


#here we are going to take the book Dracula and use split() which will create a list of all the words 
#whereever it finds a space.

filename = "dracula.txt"

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry {filename} can not be found in working directory.")
else:
    #Count the approximate number of words in the file
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")


#lets turn this counting words in a book into a function and download some more books.

def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry can not find {filename} in the working directory")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The book {filename} has about {num_words} words in it!")

filename = "frankenstein.txt"
count_words(filename)
count_words("dracula.txt")
print()

#Lets try multiple books in a list
filename = ["dracula.txt", "frankenstein.txt", "intentionallymissing.txt", "dunwichhorror.txt"]
for file in filename:
    count_words(file)

#sometimes you just want to fail in silence, in which case just place a pass in except
def count_words_in_book(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The book {filename} has about {num_words} words in it!")

filename = ["dracula.txt", "frankenstein.txt", "intentionallymissing.txt", "dunwichhorror.txt"]

for file in filename:
    count_words_in_book(file)

#Addition: One common problem when prompting for numerical input occurs when
#people provide text instead of numbers. When you try to convert the input to an int, you’ll get
#a ValueError. Write a program that prompts for two numbers. Add them together and print
#the result. Catch the ValueError if either input value is not a number, and print a friendly error
#message. Test your program by entering two numbers and then by entering some text instead
#of a number.
while True:
    number_one = input("What is the first number you would like to add? Enter to quit. ") #should really be testing for int here
    if number_one == '':
        break
    number_two = input("What is the second number you would like to add? Enter to quit. ")
    if number_two == '':
        break
    try:
        value = int(number_one) + int(number_two)
    except ValueError:
        print("Please enter a number ")
    else:    
        print(value)

#Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three names of cats in
#the first file and three names of dogs in the second file. Write a program that tries to read these
#files and print the contents of the file to the screen. Wrap your code in a try-except block to
#catch the FileNotFound error, and print a friendly message if a file is missing. Move one of the
#files to a different location on your system, and make sure the code in the except block
#executes properly.
catfile = "catfile.txt"
dogfile = "dogfile.txt"

with open(catfile, 'w') as file_object:
    cat_content = file_object.write("Pork Chop\nTiger\nLa'FaShe")

with open(dogfile, 'w') as f:
    dog_content = f.write("Barney\nJack\nDuke")

try:
    with open(catfile) as file_object:
        cat_read = file_object.read()
except FileNotFoundError:
    print(f"Can't find {catfile} in the working directory.")
else:
    print(cat_read)

print()

try:
    with open(dogfile) as file_object:
        dog_read = file_object.read()
except FileNotFoundError:
    print(f"Can't find {dogfile} in the working directory.")
else:
    print(dog_read)

#Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail silently if
#either file is missing.
catfile = "catfile.txt"
dogfile = "dogfile.txt"

with open(catfile, 'w') as file_object:
    cat_content = file_object.write("Pork Chop\nTiger\nLa'FaShe")

with open(dogfile, 'w') as f:
    dog_content = f.write("Barney\nJack\nDuke")

try:
    with open(catfile) as file_object:
        cat_read = file_object.read()
except FileNotFoundError:
    pass
else:
    print(cat_read)

print()

try:
    with open(dogfile) as file_object:
        dog_read = file_object.read()
except FileNotFoundError:
    pass
else:
    print(dog_read)

#Common Words: Visit Project Gutenberg (https://gutenberg.org/) and find a few texts
#you’d like to analyze. Download the text files for these works, or copy the raw text from your
#browser into a text file on your computer.
#You can use the count() method to find out how many times a word or phrase appears in a
#string. For example, the following code counts the number of times 'row' appears in a string:
#>>> line = "Row, row, row your boat"
#>>> line.count('row')
#2
#>>> line.lower().count('row')
#Notice that converting the string to lowercase using lower() catches all appearances of the
#word you’re looking for, regardless of how it’s formatted.
#Write a program that reads the files you found at Project Gutenberg and determines how
#many times the word 'the' appears in each text. This will be an approximation because it will
#also count words such as 'then' and 'there'.

book_name = "dracula.txt"

with open(book_name, encoding='utf-8') as file_object:
    content = file_object.read()

words = content.split()
num_words = words.count("the")
print(num_words)
num_words = words.count("and")
print(num_words)
num_words = words.count("bat")
print(num_words)
num_words = words.count("girl")
print(num_words)
num_words = words.count("castle")
print(num_words)

#Common Words: Visit Project Gutenberg (https://gutenberg.org/) and find a few texts
#you’d like to analyze. Download the text files for these works, or copy the raw text from your
#browser into a text file on your computer.
#You can use the count() method to find out how many times a word or phrase appears in a
#string. For example, the following code counts the number of times 'row' appears in a string:
#>>> line = "Row, row, row your boat"
#>>> line.count('row')
#2
#>>> line.lower().count('row')
#Notice that converting the string to lowercase using lower() catches all appearances of the
#word you’re looking for, regardless of how it’s formatted.
#Write a program that reads the files you found at Project Gutenberg and determines how
#many times the word 'the' appears in each text. This will be an approximation because it will
#also count words such as 'then' and 'there'.

book_name = "dracula.txt"

with open(book_name, encoding='utf-8') as file_object:
    content = file_object.read()

words = content.split()
num_words = words.count("the")
print(num_words)
num_words = words.count("and")
print(num_words)
num_words = words.count("bat")
print(num_words)
num_words = words.count("girl")
print(num_words)
num_words = words.count("castle")
print(num_words)

#the JSON module allows you to dump simple python data structures into a file
#you can load, share that file between different python programs
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f) #dumbs numbers list into f

#now we'll load that list back into memory
with open(filename) as f:
    numbers = json.load(f)

print(numbers)

#Saving data is usefule when you're working with user generated data because if you don't store that data somehow
#you'll lose it when the program stops running.
#lets create a program that will prompt for a name the first time they run a program and then remember next time the program is run
import json

username = input("what is your name? ")

filename = "username.json"
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back {username.title()}!")

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username.title()}!")

print()
#We need to combine these two programs above into one file. When someone
#runs remember_me.py, we want to retrieve their username from memory if
#possible; therefore, we’ll start with a try block that attempts to recover theusername. If the file username.json doesn’t exist, we’ll have the except block
#prompt for a username and store it in username.json for next time:
import json

filename = "username.json"
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back {username.title()}")
else:
    print(f"Welcome back, {username}!")

#Favorite Number: Write a program that prompts for the user’s favorite number. Use
#json.dump() to store this number in a file. Write a separate program that reads in this value
#and prints the message, “I know your favorite number! It’s _____.”
import json
filename = "favnumber.txt"

fav_number = input("What is your favourite number? ")

with open(filename, 'w') as f:
    json.dump(fav_number, f)

with open(filename) as f:
    num = json.load(f)
    print(f"I know your fav number is {num}!")

#Favorite Number Remembered: Combine the two programs from Exercise 10-11
#into one file. If the number is already stored, report the favorite number to the user. If not,
#prompt for the user’s favorite number and store it in a file. Run the program twice to see that it
#works.
import json

filename = "tendashtwo.json"

try:
    with open(filename) as f:
        favs = json.load(f)
except FileNotFoundError:
    num_be = input("What is your fav number? ")
    with open(filename, 'w') as f:
        json.dump(num_be, f)
else:
    print(f"Your fav numb exists and it is {favs}!")

#Verify User: The final listing for remember_me.py assumes either that the user has
#already entered their username or that the program is running for the first time. We should
#modify it in case the current user is not the person who last used the program.
#Before printing a welcome back message in greet_user(), ask the user if this is the correct
#username. If it’s not, call get_new_username() to get the correct username.
import json

filename = "remember.json"

def get_new_username():
    who = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(who, f)
        print(f"Hello {who.title()}.")

try:
    with open(filename) as f:
        person = json.load(f)
except FileNotFoundError:
    get_new_username()    
else:
    test_name = input(f"Are you person {person.title()}? ")
    if test_name == 'yes':
        print(f"Welcome back {person.title()}")
    elif test_name == 'no':
        get_new_username()

#continue on page 284