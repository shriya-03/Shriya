def sum_digits(n):
    return sum(int(d) for d in str(n))

print(sum_digits(1234))  # Output: 10

#def sum_digits(n):
#def means define a function.
#sum_digits is the name of the function.
#(n) is a parameter, meaning the function takes a number n as input.
# This line defines a function that will return the sum of the digits in number n.

#return sum(int(d) for d in str(n))
#Let's go step-by-step through the inner parts:

#str(n)
#Converts the number n to a string.

#Example: 1234 becomes "1234"

#for d in str(n)
#This is a loop that goes through each character (d) in the string "1234".

#So, it loops through: '1', '2', '3', '4'

#int(d)
#Converts each character back to an integer.

#'1' → 1, '2' → 2, etc.
#sum(...)
#Adds up all the integers created by the loop.

#So it calculates: 1 + 2 + 3 + 4 → 10

