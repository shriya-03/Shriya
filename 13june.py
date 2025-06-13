def findAllOccurrences(text: str, pattern: str) -> list:
    indices = []
    n, m = len(text), len(pattern)
    if m == 0:
        # By definition, every index is a valid start for an empty pattern.
        return list(range(n))
    
    # Check every possible starting point.
    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            indices.append(i)
    return indices

# Example usage:
print(findAllOccurrences("abracadabra", "abra"))  # Output: [0, 7]


#All Occurrences of a Pattern in a String
#Whenever the substring of the text matches the pattern, the function 
# records the starting position of that substring (the index in the text where the match begins).
#If a match is found, the starting index is stored.