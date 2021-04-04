#Write a function named collatz() that has a parameter named number.
#IF the number is even then the function should print number // 2 and return the value
#if the number is odd then the function should print and return 3 * number + 1
#then write a program that lets a user pick an integer and keeps calling collatz on that number until the function returns the value 1
#Add try and except statements

def collatz(number):
    
    if number % 2 == 0:
        print(number // 2)
        return number // 2

    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result

n = int(input("Give me a number: "))
while n != 1:
    n = collatz(n)


