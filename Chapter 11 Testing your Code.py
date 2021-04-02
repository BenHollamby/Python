#to learn about testing first we need some code to test
#here is a simple function that we will test
def get_formatted_name(first, last):
    full_name = f"{first} {last}"
    return full_name.title()

#and here is a simple program that uses this function
print("Press enter to quit at any time")
while True:
    first = input("First name? ")
    if first == '':
        break
    last = input("Last name? ")
    if last == '':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")

#So we run the above and we know it works, but running it several times can be tedious
#the module unittest provides tools to test your code
#The syntax for setting up a test case takes some getting used to, but once
#you’ve set up the test case it’s straightforward to add more unit tests for your
#functions. To write a test case for a function, import the unittest module and
#the function you want to test. Then create a class that inherits from
#unittest.TestCase, and write a series of methods to test different aspects of your
#function’s behavior.
#Here’s a test case with one method that verifies that the function
#get_formatted_name() works correctly when given a first and last name:

#also updating the function | if looking at, seperate into two files so you can import
def get_formatted_names(first, last, middle=''):
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()


import unittest
#from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    def test_first_middle_last_name(self):
        formatted_name = get_formatted_names('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()

#City, Country: Write a function that accepts two parameters: a city name and a country
#name. The function should return a single string of the form City, Country, such as
#Santiago, Chile. Store the function in a module called city_functions.py.
#Create a file called test_cities.py that tests the function you just wrote (remember that you
#need to import unittest and the function you want to test). Write a method called
#test_city_country() to verify that calling your function with values such as 'santiago' and
#'chile' results in the correct string. Run test_cities.py, and make sure test_city_country()
#passes.
def city_country(city, country):
    city_name = f"{city}, {country}"
    return(city_name.title())

import unittest
from city_functions import city_country

class CityTestCase(unittest.TestCase):

    def test_city_country(self):
        string_city = city_country('minsk', 'russia')
        self.assertEqual(string_city, 'Minsk, Russia')

if __name__ == "__main__":
    unittest.main()

############################################################################################
#Population: Modify your function so it requires a third parameter, population. It
#should now return a single string of the form City, Country – population xxx, such as
#Santiago, Chile – population 5000000. Run test_cities.py again. Make sure
#test_city_country() fails this time.Modify the function so the population parameter is optional. Run test_cities.py again, and
#make sure test_city_country() passes again.
#Write a second test called test_city_country_population() that verifies you can call your
#function with the values 'santiago', 'chile', and 'population=5000000'. Run test_cities.py
#again, and make sure this new test passes.
def city_country(city, country, population=''):
    if population:
        city_name = f"{city}, {country} has a population of {population}."
    else:
        city_name = f"{city}, {country}"
    return(city_name.title())

import unittest
from city_functions import city_country

class CityTestCase(unittest.TestCase):

    def test_city_country(self):
        string_city = city_country('moscow', 'russia')
        self.assertEqual(string_city, 'Moscow, Russia')

    def test_city_country_population(self):
        string_city = city_country('minsk', 'russia', '1975000')
        self.assertEqual(string_city, 'Minsk, Russia Has A Population Of 1975000.')

if __name__ == "__main__":
    unittest.main()

#continue on 292