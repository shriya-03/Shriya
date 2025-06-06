import re

def is_valid_palindrome(s: str) -> bool:
    # Remove all non-alphanumeric characters and convert to lowercase.
    cleaned_str = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    
    # Check if the cleaned string is the same forwards and backwards.
    return cleaned_str == cleaned_str[::-1]

# Testing the function:
print(is_valid_palindrome("A man, a plan, a canal: Panama"))  # Output: True
print(is_valid_palindrome("race a car"))                      # Output: False

# palindrome — that means it reads the same forwards and backwards 
# ignoring spaces, punctuation, and capitalization
#To do this, you clean the string:

#Remove everything that's not a letter or number (like commas, spaces, colons)
#Convert all letters to lowercase so that 'A' and 'a' are treated the same.
#We use a tool called a regular expression (re.sub) to do that in one step.

#Now compare it with its reverse (the same string but backward):
#Original: "amanaplanacanalpanama"
#Reversed: "amanaplanacanalpanama"
#If they're the same, it’s a palindrome

