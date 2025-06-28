def square_array(arr):
    return [x ** 2 for x in arr]

print(square_array([2, 3, 4]))  # Output: [4, 9, 16]

#def square_array(arr):
#This line defines a function named square_array.
#The function takes one argument called arr, which is expected to be a list of numbers.

#return [x ** 2 for x in arr]
#This is a list comprehension, a concise way to create a new list.
#x for x in arr: loops over each element x in the input list arr.
#x ** 2: squares each number (x raised to the power of 2).
#The result is a new list where each element is the square of the corresponding element in arr.
#Example: if arr = [2, 3, 4], the new list will be [2**2, 3**2, 4**2] → [4, 9, 16].

#print(square_array([2, 3, 4]))
#This line calls the square_array function with [2, 3, 4] as input.
#It prints the result of the function, which is [4, 9, 16].