def circular_get(lst, pos):
    return lst[(pos - 1) % len(lst)]

print(circular_get(["a", "b", "c"], 4))  # "a"

#def defines a function named circular_get.
#It takes two arguments:
#lst: a list of elements (e.g., ["a", "b", "c"])
#pos: the position you want to access in a circular way (i.e., wrap around if it goes beyond the list)

#pos - 1:
#This converts 1-based indexing (human style, where position 1 is 
# the first element) to 0-based indexing (Python style).
#Example: if pos = 4, then 4 - 1 = 3

#len(lst):
#Gets the number of elements in the list. For ["a", "b", "c"], it’s 3.
#(pos - 1) % len(lst):
#This uses modulo (%) to "wrap around" if the index is out of bounds.
#3 % 3 = 0, so it wraps around to the start of the list.

#lst[...]:
#Accesses the element at the resulting index.
#So, lst[(4 - 1) % 3] = lst[3 % 3] = lst[0] = "a"