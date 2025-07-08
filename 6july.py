def counter_effect(digits):
    return [list(range(int(d) + 1)) for d in digits]

# Example usage
print(counter_effect("1250"))  # [[0, 1], [0, 1, 2], [0, 1, 2, 3, 4, 5], [0]]
counter_effect("1250")
# => [
#   [0, 1],           # 1 → [0, 1]
#   [0, 1, 2],        # 2 → [0, 1, 2]
#   [0, 1, 2, 3, 4, 5],# 5 → [0, 1, 2, 3, 4, 5]
#   [0]               # 0 → [0]
# ]
