# Compute n! (factorial of n).
# Take each digit of the result and square it.
# Sum those squares.
# Return the smallest integer greater than or equal to the square root of that sum.

import math
import math

def factorial_digit_square(n: int) -> int:
    fact_str = str(math.factorial(n))
    total = sum(int(d)**2 for d in fact_str)
    return math.isqrt(total) if math.isqrt(total)**2 == total else math.isqrt(total)+1

print(factorial_digit_square(5))  # 5! = 120 → 1²+2²+0²=5 → sqrt(5)=2.23 → 3
print(factorial_digit_square(6))  # 6! = 720 → 7²+2²+0²=53 → sqrt(53)=7.28 → 8



# math.isqrt(x) gives the integer part of sqrt(x) (like floor(sqrt(x)))
# If isqrt(x)**2 == x, then x is a perfect square → return isqrt(x)
# Otherwise, we return isqrt(x) + 1 to get the ceiling of the square root.