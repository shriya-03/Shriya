def two_sum(nums, target):
    # Dictionary to store number -> index mapping
    lookup = {}
    # Loop over each index and number in nums
    for i, num in enumerate(nums):
        # Calculate what number is needed to reach target
        complement = target - num
        # Check if complement exists in dictionary
        if complement in lookup:
            return [lookup[complement], i]
        # Otherwise, add the current number with its index to dictionary
        lookup[num] = i

# Example usage:
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]
