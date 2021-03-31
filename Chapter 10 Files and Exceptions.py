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

#continue on page 270
           