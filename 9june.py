def longest_common_suffix(strs):
    if not strs:
        return ""
    
    # Reverse each string to transform the suffix problem into a prefix problem.
    reversed_strs = [s[::-1] for s in strs]
    
    # Use the vertical scanning method on the reversed strings.
    for i in range(len(reversed_strs[0])):
        char = reversed_strs[0][i]
        for s in reversed_strs[1:]:
            if i >= len(s) or s[i] != char:
                # Once the common prefix (of the reversed strings) ends, reverse it to get the suffix.
                return reversed_strs[0][:i][::-1]
    return reversed_strs[0][::-1]

# Example usage:
print(longest_common_suffix(["running", "jogging", "walking"]))  # Output: "ing"

#Reversing Strategy: By reversing every string, the longest common suffix of the 
#original set becomes the longest common prefix of these reversed strings.

#Vertical Scanning on Reversed Strings: The same technique as the Longest Common 
# Prefix is applied. We check each character in the reversed first string against 
# the others. When a mismatch is found, the accumulated common part of the reversed 
# strings is reversed to produce the suffix for the original strings.

