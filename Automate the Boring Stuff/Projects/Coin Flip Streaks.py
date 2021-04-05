import random

number_of_flips = 0
giant_list = []
while number_of_flips != 100:

    r = random.randint(0,1)
    number_of_flips += 1
    giant_list.append(r)
    

print(giant_list)
