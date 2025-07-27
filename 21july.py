def multiples(m, n):
    return [n * i for i in range(1, m + 1)]
print(multiples(3, 5.0))  # Output: [5.0, 10.0, 15.0]

# range(1, m + 1) generates the numbers 1 through m

# Each is multiplied by n to get the correct multiple