def lengthOfLongestWord(s: str) -> int:
    # Trim the string and split into words.
    words = s.strip().split()
    # Find the length of the longest word.
    return max(len(word) for word in words)

# Example usage:
print(lengthOfLongestWord("The quick brown fox jumps over the lazy dog "))  # Output: 5

#Given a string s made up of words separated by spaces, return the length of 
# the longest word in the string.
#Step 1: s.strip().split()
#strip() removes any leading or trailing spaces from the string.
#Example: " hello world " becomes "hello world"
#split() splits the string by spaces into a list of words.
#Example: "The quick brown" becomes ["The", "quick", "brown"]

# Step 2: max(len(word) for word in words)
#This is a generator expression that:
#Loops over each word in the list.
#Applies len(word) to get the length of each word.
#Then max() finds the largest of those lengths.