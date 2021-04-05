#Write a function that takes a list value as an argument and returns a string with all the items separated by
#a comma and a space with 'and' inserted before the last item
#be sure to test an empty list

spam = ['apples', 'bananas', 'tofu', 'cats']
red_list = []

print(spam)

def string_and(mylist):
    if mylist:
        last_item = mylist.pop()
        x = ", ".join(mylist)
        print(f"{x} and {last_item}")
    else:
        print("Empty list yo!")

string_and(spam)
string_and(red_list)