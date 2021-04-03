#You can model almost anything with classes. In this example we'll 'Class' a dog.
#Not a class that represents a particular dog, but any dog
#We know most dogs have a name and age and a behavior of sit and roll over
#each instance created from the dog class will store a name and an age and we'll give each dog the ability to sit and roll over

class Dog:
    
    """a simple attempt to model a dog"""

    def __init__(self, name, age):

        """initalise name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):

        """simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):

        """simulate a dog rolling over in response to a command"""
        print(f"{self.name} rolled over!")

my_dog = Dog('Jack', 4)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog's age is {my_dog.age} years old!")
print()

#And here is how to call the methods (functions) in the class Dog
my_dog.sit()
my_dog.roll_over()

#create a class that contains two attributes name and cuisine, make a method called describe_restaurant that prints this info
# create a method called open_restaurant that prints a message saying the restaurant is open
# create three restaurants

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\n{self.restaurant_name.title()} is a {self.cuisine_type.title()} restaurant.")

    def is_open(self):
        print(f"{self.restaurant_name.title()} is open.\n")

dinner = Restaurant('sum king', 'korean')

dinner.describe_restaurant()
dinner.is_open()

dinner1 = Restaurant('noodle king', 'thai')
dinner1.describe_restaurant()
dinner1.is_open()

dinner2 = Restaurant('kfc', 'garbage but delicious')
dinner2.describe_restaurant()
dinner2.is_open()

#Make a class called User. Create two attributes called first_name and last_name,
#and then create several other attributes that are typically stored in a user profile. Make a
#method called describe_user() that prints a summary of the user’s information. Make another
#method called greet_user() that prints a personalized greeting to the user.
#Create several instances representing different users, and call both methods for each user.

class User:

    def __init__(self, first_name, last_name, age, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.occupation = occupation
    
    def describe_user(self):
        print(f"User's name: {self.first_name.title()} {self.last_name.title()}\n\tAge: {self.age}\n\tOccupation: {self.occupation.title()}")

    def greet_user(self):
        print(f"\nWell hello there {self.first_name.title()} {self.last_name.title()}\n")

my_user = User('ben', 'james', 27, 'information technology')
my_user.describe_user()
my_user.greet_user()

#Start with your program from Exercise 9-1 (page 162). Add an attribute
#called number_served with a default value of 0. Create an instance called restaurant from this
#class. Print the number of customers the restaurant has served, and then change this value and
#print it again.
#Add a method called set_number_served() that lets you set the number of customers that
#have been served. Call this method with a new number and print the value again.
#Add a method called increment_number_served() that lets you increment the number of
#customers who’ve been served. Call this method with any number you like that could represent
#how many customers were served in, say, a day of business.
class Restaurants:
    
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"\n{self.restaurant_name.title()} is a {self.cuisine_type.title()} restaurant and has served {self.number_served} customers so far.")

    def is_open(self):
        print(f"{self.restaurant_name.title()} is open.\n")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, inc_number):
        self.number_served += inc_number

dinners = Restaurants('sum king', 'korean')
dinners.set_number_served(1)
dinners.describe_restaurant()
dinners.increment_number_served(15)
dinners.describe_restaurant()


#Login Attempts: Add an attribute called login_attempts to your User class from
#Exercise 9-3 (page 162). Write a method called increment_login_attempts() that increments
#the value of login_attempts by 1. Write another method called reset_login_attempts() that
#resets the value of login_attempts to 0.
#Make an instance of the User class and call increment_login_attempts() several times.
#Print the value of login_attempts to make sure it was incremented properly, and then call
#reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.
class Users:

    def __init__(self, username, login_attempts=0):
        self.username = username
        self.login_attempts = 1

    def describes_user(self):
        print(f"{self.username.title()} has logged in {self.login_attempts} times!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

calling_name = Users('benholla')
calling_name.increment_login_attempts
calling_name.describes_user()
calling_name.increment_login_attempts()
calling_name.describes_user()
calling_name.increment_login_attempts()
calling_name.describes_user()
calling_name.increment_login_attempts()
calling_name.describes_user()
calling_name.increment_login_attempts()
calling_name.describes_user()

calling_name.reset_login_attempts()
calling_name.describes_user()

#Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called
#IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 162) or
#Exercise 9-4 (page 167). Either version of the class will work; just pick the one you like better.
#Add an attribute called flavors that stores a list of ice cream flavors. Write a method thatdisplays these flavors. Create an instance of IceCreamStand, and call this method.
class Icecreamstand(Restaurant):
    
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)

    def flavors(self):
        flavor_list = ['strawberry', 'trumpet', 'gum drops']
        print("Our current selection of flavours are:")
        for flavor in flavor_list:
            print(f"\t{flavor}")


creamy = Icecreamstand('bens', 'ice cream')

creamy.describe_restaurant()
creamy.is_open()
creamy.flavors()

#Admin: An administrator is a special kind of user. Write a class called Admin that inherits
#from the User class you wrote in Exercise 9-3 (page 162) or Exercise 9-5 (page 167). Add an
#attribute, privileges, that stores a list of strings like "can add post", "can delete post",
#"can ban user", and so on. Write a method called show_privileges() that lists the
#administrator’s set of privileges. Create an instance of Admin, and call your method.
class Admin(User):
    
    def __init__(self, first_name, last_name, age, occupation):
        super().__init__(first_name, last_name, age, occupation)
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    
    def show_privileges(self):
        permissions = self.privileges
        print(f"{self.first_name.title()} {self.last_name.title()} has the following permissions") 
        for p in permissions:
            print(f"\t{p}")

ituser = Admin('ben', 'holla', 27, 'information technology')

ituser.show_privileges()

#Dice: Make a class Die with one attribute called sides, which has a default value of 6.
#Write a method called roll_die() that prints a random number between 1 and the number of
#sides the die has. Make a 6-sided die and roll it 10 times.
#Make a 10-sided die and a 20-sided die. Roll each die 10 times.
from random import randint

class Die:

    def __init__(self, sides):
        self.sides = sides
    
    def roll_die(self):
        print(randint(1,self.sides))

tyeee = Die(6)
tyeee.roll_die()
tyeee.roll_die()

tyeeeee = Die(10)
tyeeeee.roll_die()
tyeeeee.roll_die()

tyeeee = Die(20)
tyeeee.roll_die()
tyeeee.roll_die()

#Lottery: Make a list or tuple containing a series of 10 numbers and five letters.
#Randomly select four numbers or letters from the list and print a message saying that any ticket
#matching these four numbers or letters wins a prize.
from random import choices

lottery_list = ['a', 'b', 'c', 'd', 'e', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

test = choices(lottery_list, k=4)
print(test)

#Lottery Analysis: You can use a loop to see how hard it might be to win the kind of
#lottery you just modeled. Make a list or tuple called my_ticket. Write a loop that keeps pulling
#numbers until your ticket wins. Print a message reporting how many times the loop had to run
#to give you a winning ticket.

from random import choices

lottery_list = ['a', 'b', 'c', 'd', 'e', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #easy to change this to nz lotto with range(1,41)

my_pick = [10, 'a', 5, 'd'] #and then pick 6 digits, could probably work out a powerball one as well. Not that it would help.

number_of_times = 0

while True:
    test = choices(lottery_list, k=4)
    if test == my_pick:
        print(f"Congrats, your numbers were rolled after {number_of_times}!")
        break
    else:
        number_of_times += 1