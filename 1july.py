def last_string_formatted(strings):
    sorted_list = sorted(strings)
    last_string = sorted_list[-1]
    return '--'.join(last_string)
words = ["zebra", "Lemon", "apple"]
result = last_string_formatted(words)
print(result)

#def last_string_formatted(strings):
#This defines a new function named last_string_formatted that takes one 
# argument: strings, which is expected to be a list of strings (e.g., ["zebra", "Lemon", "apple"]).

#sorted_list = sorted(strings)
#This line sorts the list strings in lexicographical (dictionary) order, and assigns the result
# to the variable sorted_list.
#Important detail: Sorting in Python is case-sensitive, so uppercase letters come before lowercase 
# ones. For example, "Lemon" comes before "apple", and both come before "zebra".

#last_string = sorted_list[-1]
#This line selects the last element in the sorted list using the [-1] index, and assigns it to 
# last_string.
#Since the list is now sorted, this will be the lexicographically largest string (according to 
# Python's default sorting rules).

# return '--'.join(last_string)
#This joins the characters of the string last_string with '--' between each character.
#For example, if last_string is "zebra", it becomes "z--e--b--r--a".

#words = ["zebra", "Lemon", "apple"]
#A list called words is defined with three strings.

#result = last_string_formatted(words)
#The function last_string_formatted is called with words as the input.
#The result (a formatted string) is stored in the variable result.

#print(result) : Prints the final formatted string to the console.

