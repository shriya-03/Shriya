def scoreboard(string):
    word_to_num = {
        'nil': 0, 'zero': 0, 'one': 1, 'two': 2, 'three': 3,
        'four': 4, 'five': 5, 'six': 6, 'seven': 7,
        'eight': 8, 'nine': 9
    }

    words = string.lower().split()
    scores = [word_to_num[word] for word in words if word in word_to_num]

    return scores if len(scores) == 2 else None

print(scoreboard("The score is four nil"))  
# Output: [4, 0]
print(scoreboard("new score: two three"))    
# Output: [2, 3]
print(scoreboard("Arsenal just conceded another goal, two nil"))  
# Output: [2, 0]


# The input string is converted to lowercase and split into individual words.
# Example: "The score is four nil" → ['the', 'score', 'is', 'four', 'nil']

# scores = [word_to_num[word] for word in words if word in word_to_num]
# The function returns the score only if it found exactly two numbers.
# Otherwise, it returns None.

# print(scoreboard("The score is four nil")) # → [4, 0]
# Found words: ['two', 'three'] → [2, 3]
# If the sentence has **more than or less than 2 valid score words**, it returns `None`.

