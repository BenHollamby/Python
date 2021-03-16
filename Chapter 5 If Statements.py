cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#run the two below in actual python shell
car = 'bmw'
car == 'bmw'

#prints True
racer = "audi"
print("\n")
print(racer == 'audi')

#prints false as compare statement has a capital
racer = "audi"
print("\n")
print(racer == 'Audi')

#prints true because variable has title appended
racer = "audi"
print("\n")
print(racer.title() == 'Audi')

#prints true because it does not equal Audi
racer = "audi"
print("\n")
print(racer != 'Audi')


alien_color = 'green'

if alien_color == 'green':
    print(True)

alien_color = 'yellow'

if alien_color == 'green':
    print(True)

print("\n")

alien_color = 'green'

if alien_color == 'green':
    print("5 points!")

if alien_color != 'green':
    print("10 points!")

if alien_color == 'green':
    print("5 points!")
else:
    print("10 points!")



alien_color = 'green'
if alien_color == 'green':
    print("\n5 points!")
elif alien_color == 'yellow':
    print("\n10 points!")
else:
    print("\n15 points!")

alien_color = 'yellow'
if alien_color == 'green':
    print("\n5 points!")
elif alien_color == 'yellow':
    print("\n10 points!")
else:
    print("\n15 points!")

alien_color = 'red'
if alien_color == 'green':
    print("\n5 points!")
elif alien_color == 'yellow':
    print("\n10 points!")
else:
    print("\n15 points!")


age = 30
if age < 2:
    print("\nPerson is a baby")
elif age >= 2 and age < 4:
    print("\nPerson is a toddler")
elif age >= 4 and age < 13:
    print("\nPerson is a kid")
elif age >= 13 and age < 20:
    print("\nPerson is a teenager")
elif age >= 20 and age < 65:
    print("\nPerson is an adult")
elif age >= 65:
    print("\nPerson is an elder")

#continue tomorrow, we are on page 140