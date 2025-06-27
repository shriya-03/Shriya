def capitalize_and_join(words):
    return ' '.join(word.capitalize() for word in words)

print(capitalize_and_join(["hello", "world","gg"]))  # Output: Hello World Gg

#This defines a function named capitalize_and_join that takes one parameter: words.
#words is expected to be a list of strings (e.g., ["hello", "world"]).

#    return ' '.join(word.capitalize() for word in words)
#This line: Uses a generator expression:

#For each word in the list words, it applies .capitalize():
#.capitalize() turns the first character of the string to uppercase, and the 
# rest to lowercase.
#Example: "hello" → "Hello", "WORLD" → "World"

#Uses ' '.join(...):
#The ' '.join(...) function takes a list (or iterable) of strings and joins them
#  into a single string, with a space ' ' as the separator.

#print(capitalize_and_join(["hello", "world"]))  # Output: "Hello World"
#What it does:
#Calls the function with the list ["hello", "world"]
#Prints the returned result: "Hello World"

