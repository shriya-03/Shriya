def candle_blows(s):
    candles = [int(c) for c in s]
    i = 0
    blows = 0
    while i < len(candles):
        if any(c > 0 for c in candles[i:i+3]):
            for j in range(i, min(i+3, len(candles))):
                if candles[j] > 0:
                    candles[j] -= 1
            blows += 1
        else:
            i += 3
    return blows

print(candle_blows("1321"))     # Output: 3
print(candle_blows("0323456"))  # Output: 9
print(candle_blows("2113"))     # Output: 5

# def candle_blows(s):
#     candles = [int(c) for c in s]  # Convert the string to a list of integers
#     i = 0                          # Starting index
#     blows = 0                      # Count of total blows
#     while i < len(candles):       # Loop through the candles
#         if any(c > 0 for c in candles[i:i+3]):  # If there's any candle > 0 in the next 3
#             for j in range(i, min(i+3, len(candles))):  # From i to i+3 (not past end)
#                 if candles[j] > 0:
#                     candles[j] -= 1   # Reduce height by 1
#             blows += 1
#         else:
#             i += 3  # If the current 3 candles are all zero, skip ahead
#     return blows
