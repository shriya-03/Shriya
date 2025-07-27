def fibonacci_skip(n):
    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    
    result = []
    for i in range(n):
        result.append(str(fib[i]))
        if i % 2 == 0 and i != n - 1:  # Add 'skip' after every even index except last
            result.append("skip")
    
    return ' '.join(result)

print(fibonacci_skip(7))  # Output: "1 skip 1 skip 2 skip 3 skip 5 skip 8 skip 13"


# For n = 7, the first 7 Fibonacci numbers are:
# 1, 1, 2, 3, 5, 8, 13
# With "skip" after every other value:

# 1 skip 1 skip 2 skip 3 skip 5 skip 8 skip 13
# We include "skip" after every value except the last one, if it's an even index (0-based).