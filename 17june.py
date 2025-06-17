def cubeRoot(x: int) -> int:
    # For small values, the cube root is the number itself.
    if x < 2:
        return x
    
    # Set search range. For x ≥ 2, the cube root is at most x.
    low, high = 1, x
    
    while low <= high:
        mid = low + (high - low) // 2
        cube = mid * mid * mid
        
        if cube == x:
            return mid
        elif cube < x:
            low = mid + 1
        else:
            high = mid - 1
    
    # high will be the largest integer such that high^3 <= x.
    return high

# Example usage:
print(cubeRoot(27))  # Output: 3
print(cubeRoot(28))  # Output: 3

#define a function that takes a non-negative integer x as input.
#If x is 0 or 1, then its cube root is x itself.
#For example: cube root of 0 is 0, and cube root of 1 is 1.

#For any number x ≥ 2, its cube root must lie between 1 and x, inclusive.
#Ymid is the middle of the current search range.
#calculate cube = mid³
#If you find an exact cube root, return it.If mid³ is too small, search in the higher half.
#If mid³ is too large, search in the lower half.
#The loop stops when low > high.At this point, high is the largest integer such that high³ ≤ x.

#adjusting the search range depending on whether the current guess (mid) is too small or too large.
#elif cube < x:
#    low = mid + 1  # Search higher
#This means the cube (mid³) is too small.
#So we move the search to the higher half → make low = mid + 1.
#This is what we mean by "search higher".

#else:
#    high = mid - 1  # Search lower
#This means the cube (mid³) is too big.
#So we move the search to the lower half → make high = mid - 1.
#This is what we mean by "search lower".





