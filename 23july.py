def encode(text):
    result = ''
    for char in text:
        if char.isalpha():
            index = ord(char.lower()) - ord('a')  # 0-based index
            result += '1' if index % 2 == 1 else '0'
        else:
            result += char
    return result

print(encode("Hello World!"))  # Output: "10110 00111!"

# Use 0-based indexing for the alphabet: 'a' = 0, 'b' = 1, ..., 'z' = 25
# Replace each letter with:
# '1' if the index is odd
# '0' if the index is even
# Non-letter characters remain unchanged
# The case (uppercase/lowercase) does not matter

# Example
# For "Hello World!":
# 'H' → index 7 → odd → '1'
# 'e' → index 4 → even → '0'
# 'l' → index 11 → odd → '1'
# 'l' → 11 → odd → '1'
# 'o' → 14 → even → '0'
# So "Hello" becomes "10110"

