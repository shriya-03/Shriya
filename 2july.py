def dash_join(arr):
    return '-'.join(str(x) for x in arr)

print(dash_join([1, 2, 3]))  # Output: "1-2-3"

#str(x) for x in arr – Generator expression
#This converts each integer in the list to a string.
#For example, [1, 2, 3] → ["1", "2", "3"]

# '-'.join(...)
#The join() method combines all the strings in the list using - as a separator.
#So "1", "2", "3" → "1-2-3" 