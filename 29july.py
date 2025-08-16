# Generate the first n Fibonacci numbers
# Concatenate them into one big string of digits
# Square each digit
# Sum those squares
# Return the ceiling of the square root of that sum


import math
def fib_digit_square(n: int) -> int:
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    
    digits = "".join(str(x) for x in fib[:n])
    total = sum(int(d)**2 for d in digits)
    
    return math.isqrt(total) if math.isqrt(total)**2 == total else math.isqrt(total)+1

print(fib_digit_square(5))  # Fib = [0,1,1,2,3]  "01123"
# digits: [0,1,1,2,3]  squares = [0,1,1,4,9] = 15  sqrt=3.87 so ceiling is  4

# math.isqrt(15) returns 3 (because √15 ≈ 3.87)
# 3² = 9  not equal to 15  not a perfect square
# So return 3 + 1 = 4