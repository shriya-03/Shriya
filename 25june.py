def invert_positives(num):
    return [-x for x in num if x > 0]

print(invert_positives([1, -3, 4, -2]))  # Output: [-1, -4]

#def invert_positives(num):
#This defines a function named invert_positives.
#It takes one argument num (a list of numbers).

#return [-x for x in num if x > 0]
#This line uses a list comprehension, which is a short way to create a list.

#for x in num → Go through each item x in the list num.
#if x > 0 → Only keep the numbers that are greater than 0 (positive numbers).
#-x → Invert the number (e.g., if x = 1, -x = -1).
