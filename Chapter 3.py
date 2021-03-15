names = ["ben", "angela", "alice"]
print(names)
print(names[0])
print(names[1])
print(names[2])

print("Hello " + names[0].title())
print("Hello " + names[1].title())
print("Hello " + names[2].title())

transportation = ["audi", "alfa romeo", "maserati"]

print("I would like to own a " + transportation[0].title())
print("I would like to own a " + transportation[1].title())
print("I would like to own a " + transportation[2].title())

dinner_list = ["ben", "angela", "alice"]

print("Hello " + dinner_list[0].title() + ", would you like to come to dinner?")
print("Hello " + dinner_list[1].title() + ", would you like to come to dinner?")
print("Hello " + dinner_list[2].title() + ", would you like to come to dinner?")

print("Unfortunately, " + names[1].title() + " can't make it for dinner")

dinner_list[1] = "fermi"

print("Hello " + dinner_list[0].title() + ", would you like to come to dinner?")
print("Hello " + dinner_list[1].title() + ", would you like to come to dinner?")
print("Hello " + dinner_list[2].title() + ", would you like to come to dinner?")

print("\nHey, " + dinner_list[0].title() + ", " + dinner_list[1].title() + ", " + dinner_list[2].title() + ", we now have a bigger table, does anyone want to invite anyone?")

dinner_list.insert(0, "kelly")
dinner_list.insert(2, "chase")
dinner_list.append("aaron")

print("\nHello " + dinner_list[0].title() + ", would you like to come to dinner?")
print("Hello " + dinner_list[1].title() + ", would you like to come to dinner?")
print("Hello " + dinner_list[2].title() + ", would you like to come to dinner?")
print("Hello " + dinner_list[3].title() + ", would you like to come to dinner?")
print("Hello " + dinner_list[4].title() + ", would you like to come to dinner?")
print("Hello " + dinner_list[5].title() + ", would you like to come to dinner?")

print("\nUnfortunately the table is not going to make it in time, and there is only space for two people :(")

dinner_list_popped = dinner_list.pop()
print("Sorry, " + dinner_list_popped + " we have to cancel your seat, I am so sorry!")
dinner_list_popped = dinner_list.pop()
print("Sorry, " + dinner_list_popped + " we have to cancel your seat, I am so sorry!")
dinner_list_popped = dinner_list.pop()
print("Sorry, " + dinner_list_popped + " we have to cancel your seat, I am so sorry!")
dinner_list_popped = dinner_list.pop()
print("Sorry, " + dinner_list_popped + " we have to cancel your seat, I am so sorry!")

print(dinner_list)

del dinner_list[-1]
print(dinner_list)
del dinner_list[-1]
print(dinner_list)