def flip(direction, columns):
    if direction == 'R':
        return sorted(columns)
    else:
        return sorted(columns, reverse=True)

# Example usage:
print(flip('R', [3, 2, 1, 2]))      # Output: [1, 2, 2, 3]
print(flip('L', [1, 4, 5, 3, 5]))   # Output: [5, 5, 4, 3, 1]

#def: This is a keyword in Python that tells the interpreter “we are defining a function.”
#flip: This is the name of the function. You can call it anything, but flip is a meaningful name here.
#direction, columns): These are the parameters the function takes.
#direction: A string that will be either 'R' or 'L', representing the direction you want to "flip" (or sort).
#columns: A list of numbers (like [3, 2, 1]) that we want to sort (or simulate flipping).

#if: This is a conditional keyword that checks if something is true.
#direction == 'R': This checks if the value of the variable direction is exactly equal to the string 'R'.
#If it is, the block under this condition will run.

#return: This sends a result back to the place where the function was called.
#sorted(columns): This sorts the list in ascending order (smallest to biggest).
#For example, if columns = [3, 2, 1, 2], it returns [1, 2, 2, 3].

#else: This means “if the if condition is not true, do this instead.”
#sorted(columns, reverse=True):
#This sorts the list in descending order (biggest to smallest).
#The reverse=True argument tells Python to flip the order after sorting.