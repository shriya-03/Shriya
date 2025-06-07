def remove_duplicates_unsorted(nums):
    seen = set()  # To track elements we've encountered.
    k = 0         # k will be our insertion index for unique elements.
    for num in nums:
        if num not in seen:
            seen.add(num)      # Mark this element as encountered.
            nums[k] = num      # Place the unique element at index k.
            k += 1             # Move the pointer for the next unique element.
    return k

# Example usage:
nums = [4, 2, 4, 3, 2, 1,6,8,8,8,1,2,4,5,5,5,5]
k = remove_duplicates_unsorted(nums)
print("New length:", k)          # Output: 7
print("Modified array:", nums[:k])  # Output:  [4, 2, 3, 1, 6, 8, 5]


#Remove Duplicates from unSorted Array (preserving order)

#As you go through each number in the array:
#If the number is not in the set, it means it’s new → keep it.
#If the number is in the set, it’s a duplicate → skip it.

#We use a pointer k to track where to put the next unique number in the array.
#Every time we find a number we haven’t seen:
#Add it to the seen set.
#Place it at index k of the array (nums[k] = num).
#Move k forward (k += 1).
#This way, all the unique values end up in the beginning of the array (from index 0 to k - 1).
