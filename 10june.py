def longest_valid_parentheses(s: str) -> int:
    max_length = 0
    # Stack to store indices of brackets.
    # Initialize with -1 to handle the edge case for valid prefix calculation.
    stack = [-1]
    
    for i, char in enumerate(s):
        if char == '(':
            # Push the index of the opening bracket.
            stack.append(i)
        else:
            # Pop the previous index.
            stack.pop()
            if not stack:
                # If stack is empty, push the current index as the new base for future valid substrings.
                stack.append(i)
            else:
                # Calculate the length of the current valid substring.
                max_length = max(max_length, i - stack[-1])
    
    return max_length

# Example usage:
print(longest_valid_parentheses("(()())"))   # Output: 6
print(longest_valid_parentheses(")()())"))   # Output: 4

#We initialize the stack with -1.
#This serves as a base index for the first valid substring.
#It helps in calculating lengths correctly when the valid substring starts at index 0.

#If the character is '(':We push its index onto the stack.
#This means we're waiting to find a matching ')' to form a valid pair.
#b. If the character is ')':We pop the top of the stack. After popping:
#If the stack is empty, it means we don’t have a matching '(' for this ')', so:
#We push the current index as a new "base" (like -1 before).
#This helps reset the base for future valid substrings.
#If the stack is not empty, we found a valid substring: