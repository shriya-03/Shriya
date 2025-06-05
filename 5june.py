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

#Given an array of integers nums and an integer target, return indices 
# of the two numbers such that they add up to target. You may assume that 
# each input would have exactly one solution, and you may not use the same
# element twice. You can return the answer in any order.

#Output: [0, 1] Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#Explanation:
#Data Structure: We use a dictionary (lookup) to record the numbers we have seen so far 
# along with their indices.

#Complement Calculation: For each number, compute its complement (i.e., target - num).

#Lookup:

#If the complement is already in our dictionary, we immediately return the pair of indices.

#If not, we add the current number and its index into the dictionary.

#Efficiency: This solution works in O(n) time since it only passes through the array once.
