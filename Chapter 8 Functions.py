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

