def int_to_roman(num: int) -> str:
    # List of tuples for values and their corresponding symbols,
    # ordered from highest to lowest. Notice the subtractive combinations.
    value_symbol = [
        (1000, "M"), (900, "CM"),
        (500, "D"),  (400, "CD"),
        (100, "C"),  (90, "XC"),
        (50, "L"),   (40, "XL"),
        (10, "X"),   (9, "IX"),
        (5, "V"),    (4, "IV"),
        (1, "I")
    ]
    
    roman = []
    # Process each value in the mapping.
    for value, symbol in value_symbol:
        # Append the symbol while subtracting its value.
        while num >= value:
            num -= value
            roman.append(symbol)
    return "".join(roman)

# Testing the function:
print(int_to_roman(3))     # Output: "III"
print(int_to_roman(58))    # Output: "LVIII"
print(int_to_roman(1994))  # Output: "MCMXCIV"

#Mapping List: We create a list of tuples pairing integer values with their 
# Roman numeral symbols. This list includes subtractive pairs (e.g., 900 -> "CM") 
# and is sorted from largest to smallest.

#Greedy Reduction: Starting from the highest value, we subtract the value as many 
# times as possible from num while appending the corresponding symbol to the result.

#Result Construction: Once num reaches 0, join the accumulated symbols to build the final 
# Roman numeral string.