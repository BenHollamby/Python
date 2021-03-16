# [] is a list
names = ["ben", "angela", "alice"]
print(names)
#using [number] grabs item in the list. Starts from 0
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

#len(names) will show how many items in a list
#str(len(names)) will turn that into a string if you want to print it
coming = str(len(dinner_list))
print("\nThere are " + coming + " people coming to dinner")

print("\nUnfortunately, " + names[1].title() + " can't make it for dinner")

#modifies the object in the list at position 1 from Alice to Fermi
dinner_list[1] = "fermi"

print("Hello " + dinner_list[0].title() + ", would you like to come to dinner?")
print("Hello " + dinner_list[1].title() + ", would you like to come to dinner?")
print("Hello " + dinner_list[2].title() + ", would you like to come to dinner?")

print("\nHey, " + dinner_list[0].title() + ", " + dinner_list[1].title() + ", " + dinner_list[2].title() + ", we now have a bigger table, does anyone want to invite anyone?")

# .inset(0, kelly) inserts name into postion zero
dinner_list.insert(0, "kelly")
dinner_list.insert(2, "chase")
#.append adds item to the end of the list
dinner_list.append("aaron")

print("\nHello " + dinner_list[0].title() + ", would you like to come to dinner?")
print("Hello " + dinner_list[1].title() + ", would you like to come to dinner?")
print("Hello " + dinner_list[2].title() + ", would you like to come to dinner?")
print("Hello " + dinner_list[3].title() + ", would you like to come to dinner?")
print("Hello " + dinner_list[4].title() + ", would you like to come to dinner?")
print("Hello " + dinner_list[5].title() + ", would you like to come to dinner?")

coming = str(len(dinner_list))
print("\nThere are " + coming + " people coming to dinner")

print("\nUnfortunately the table is not going to make it in time, and there is only space for two people :(")

# dinner_list.pop() removes the last item from the list. In the below case we are taking that last item and putting it into a variable so we can inform user of cancelation
dinner_list_popped = dinner_list.pop()
print("Sorry, " + dinner_list_popped + " we have to cancel your seat, I am so sorry!")
dinner_list_popped = dinner_list.pop()
print("Sorry, " + dinner_list_popped + " we have to cancel your seat, I am so sorry!")
dinner_list_popped = dinner_list.pop()
print("Sorry, " + dinner_list_popped + " we have to cancel your seat, I am so sorry!")
dinner_list_popped = dinner_list.pop()
print("Sorry, " + dinner_list_popped + " we have to cancel your seat, I am so sorry!")

coming = str(len(dinner_list))
print("\nThere are " + coming + " people coming to dinner")

print(dinner_list)

# del in combination with [-1] deletes the last item in the list
del dinner_list[-1]
print(dinner_list)
del dinner_list[-1]
print(dinner_list)

locations = ["antarctica", "siberia", "russia", "egypt", "jordan"]
print(locations)
#alphabetically sorts locations, not permanent
print(sorted(locations))
print(locations)
#reverse=True sorts locations variables not permanent
print(sorted(locations, reverse=True))
print(locations)
# reverse reverses the list permanently
locations.reverse()
print(locations)
locations.reverse()
print(locations)
# .sort sorts the list alphabetically permanent
locations.sort()
print(locations)
#.sort(reverse=True) sorts list in reverse alphabetical permanently
locations.sort(reverse=True)
print(locations)
