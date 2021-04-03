#create a variable
p_name = 'Ben'

#print() print string hello, with variable p_name
print("Hello " + p_name + "!")

# .upper() makes all capitals
print(p_name.upper())
#.lower() makes all lowercase
print(p_name.lower())
#.title() capitalises first letter of each word
print(p_name.title())

print('a famous person once said "that aint me"')

famous_person = "lord raiden"
print(famous_person + ' once said, "That aint me"')

message = ' once said, "That aint me"'
print(famous_person.title() + message)

print("Python")
#\t adds a tab space
print("\tPython")
#\n makes a new line
print(f'\t{famous_person},' + f'\n {message}')

white_space = "   Ben  . "

print(white_space)

#lstrip() strips any whitespace on the left, rstrip() strips from the right, strip() removes all white space
print(white_space.lstrip())
print(white_space.rstrip())
print(white_space.strip())

