pizzas = ["hawaiian", "meatlovers", "pepperoni"]
#using for, in, loops through each pizza
for pizza in pizzas:
    print(pizza)

#for loop with a statement
for pizza in pizzas:
    print(f"freaking love {pizza} type")
print("\nI really like pizza\n")

animals = ["dog", "cat", "ferret"]
for animal in animals:
    print(f"A {animal} would make a great pet!")
print("\nAny of these animals would make a great pet!\n")

#print number 1 through to number 20
digits = range(1, 21)
for digit in digits:
    print(digit)

#print number 1 through to a million | greening out cause takes too long
digits = range(1,1000001)
#for digit in digits:
#   print(digit)

#min is lowest digit
print(min(digits))
#max is highest digit
print(max(digits))
#sum is total number
print(sum(digits))

#print out odd numbers
odd_numbers = list(range(1,21,2))
print(odd_numbers)

threes = range(3,31,3)
for three in threes:
    print(three)

cubes = range(1,11)
for cube in cubes:
    print(cube ** 3)

#list comprehension (need to understand better)
cubestwo = [value**3 for value in range(1, 11)]
print(cubestwo)

names = ["ben", "angela", "alice", "kelly", "elisha", "natalie"]
print(f"The first three names in the list are {names[:3]}")
print(f"the two names in the middle are {names[2:4]}")
print(f"The last three names in the list are {names[-3:]}")

#make a copy of the above pizza's list using var = oldvar[:]
friend_pizzas = pizzas[:]

pizzas.append("stuffed crust")
friend_pizzas.append("honey chicken bacon")

print(friend_pizzas)
print(pizzas)

for pizza in pizzas:
    print(f"another of my favourite pizza is {pizza.title()}")

for friends in friend_pizzas:
    print(f"My friends favourite pizzas are {friends.title()}")

#tuple (immutable list, try popping and item it will error, but you can modify with new variable)
foods = ("korean", "thai", "sushi", "bbq", "honey soy chicken")

for food in foods:
    print(food.title())

foods = ("korean", "thai", "sushi", "satay chicken", "bbq chicken")
for food in foods:
    print(food.title())