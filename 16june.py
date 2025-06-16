def addBinary(a: str, b: str) -> str:
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    result = []
    
    while i >= 0 or j >= 0 or carry:
        # Get the current digits (0 if index is out of range)
        sum = carry
        if i >= 0:
            sum += int(a[i])
            i -= 1
        if j >= 0:
            sum += int(b[j])
            j -= 1
        
        # Compute the result digit and update carry.
        result.append(str(sum % 2))
        carry = sum // 2
    
    # The result is built in reverse order.
    return ''.join(result[::-1])

# Example usage:
print(addBinary("11", "1"))  # Output: "100"
print(addBinary("1010", "1011"))  # Output: "10101"


#Given two binary strings a and b, return their sum as a binary string.
#a = "11"   # binary 3
#b = "1"    # binary 1
#Result: "100" (binary 4)

#i and j point to the last digit (rightmost bit) of a and b.
#carry stores the carry-over from each bit addition.
#result stores the computed bits (in reverse order).

#Continue looping as long as:
#There are still digits in a or b, or
#There's a carry left to process.

#Convert characters '0' or '1' to integers.Add them along with the carry.

#sum % 2 gives the binary digit (0 or 1). sum // 2 gives the new carry (0 or 1).

#The result is built from right to left, so reverse it at the end.S