def rearrange_string(s, indices):
    result = [''] * len(s)  # Create a list of empty strings with same length as s
    for char, idx in zip(s, indices):
        result[idx] = char  # Place each character at the correct index
    return ''.join(result)  # Convert the list back to a string

print(rearrange_string("abcd", [0, 3, 1, 2]))  # Output: "acdb"
