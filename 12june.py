def moveZeroes(nums):
    # Pointer to track the next position for a non-zero element.
    j = 0
    for num in nums:
        if num != 0:
            nums[j] = num
            j += 1

    # After all non-zero elements have been moved to front,
    # fill the rest of the array with zeros.
    for i in range(j, len(nums)):
        nums[i] = 0

# Example usage:
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]


#use a pointer j to track where the next non-zero element should go.
#Loop through each element num in the array:
#If num != 0, assign it to nums[j] and increment j.

#Now that all non-zero elements are in the front, and j = 3:
#Fill the rest of the array (from index j to end) with zeros.