def two_highest(lst):
    return sorted(set(lst), reverse=True)[:2]

# Test cases
print(two_highest([4, 10, 10, 9]))  # Output: [10, 9]
print(two_highest([1, 1, 1]))       # Output: [1]
print(two_highest([]))             # Output: []

#set(lst):
#Removes duplicates → only keeps unique values.
#sorted(..., reverse=True):
#Sorts the unique values from highest to lowest.

#[:2]:
#Picks the top 2 highest values.
#If less than 2 values exist, it returns as many as possible.