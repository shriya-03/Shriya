def seven(m):
    steps = 0
    while m >= 100:  # Continue until number is at most 2 digits
        last_digit = m % 10
        m = m // 10 - 2 * last_digit
        steps += 1
    return [m, steps]

print(seven(371))        # Output: [35, 1]
print(seven(1603))       # Output: [7, 2]
print(seven(372))        # Output: [33, 1]
print(seven(477557101))  # Output: [28, 7]

# 160 - (2×3) = 160 - 6 = 154

# 15 - (2×4) = 15 - 8 = 7 → Done

# Result: [7, 2]