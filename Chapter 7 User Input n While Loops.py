#ask for input and stored as a variable
car = input("What kind of rental car are you after sir/maam? ")
print(f"Let me see if I can find you a {car.title()}")

#ask how many people are coming for dinner, if more than 8 they will have to wait
#else their table is ready | You need to convert input string to an interget with int(variable)
dinner_seats = input("How many people are coming for dinner? ")
if int(dinner_seats) > 8:
    print("Sorry you will have to wait a bit longer")
else:
    print(f"Your table for {dinner_seats} is ready")

#module % is super handy, divides one number by another and returns the remainder
#using | if number % 2 == 0 | if it is true, number is even. if not true the number is odd.
#ask for a number and report back whether the number is a multiple of 10.

number = input("What is the number to check? ")
if int(number) % 10 == 0:
    print(f"{number} is a multiple of 10!")
else:
    print(f"{number} is not a multiple of 10.")

