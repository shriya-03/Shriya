def findMin(nums):
    low, high = 0, len(nums) - 1
    
    # If the array is not rotated (the smallest value is at the beginning).
    if nums[low] <= nums[high]:
        return nums[low]
    
    while low < high:
        mid = low + (high - low) // 2
        # Compare middle element with the high to determine which side the minimum is on.
        if nums[mid] > nums[high]:
            # Minimum must be to the right of mid.
            low = mid + 1
        else:
            # Minimum could be at mid or to the left.
            high = mid
    return nums[low]

# Example usage:
print(findMin([4,5,6,7,0,1,2]))  # Output: 0

#You are given a sorted array that has been 
# rotated at some unknown pivot. The goal is to find the minimum element in this rotated array.

#define two pointers: low at the beginning and high at the end of the array.
#If the array has not been rotated, it means the first element is the smallest.
#For example, in [1, 2, 3, 4], 1 <= 4, so return 1.

#calculate the middle index between low and high.
# If nums[mid] > nums[high], this means:
#The smallest value must be to the right of mid.
#So, we move low to mid + 1.
#If nums[mid] <= nums[high]:
#The smallest value is at mid or to the left.
#So, we move high to mid.This keeps shrinking the search space until low equals high.
#When the loop ends, low points to the minimum element.
