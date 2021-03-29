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

#continue from page 235