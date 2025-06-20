def intersection(nums1, nums2):
    i, j = 0, 0
    result = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            result.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return result

# Example usage:
print(intersection([1, 2, 2, 3, 4], [2, 2, 3, 5]))  # Output: [2, 2, 3]

#Given two sorted arrays, return their intersection, i.e., 
# the common elements that appear in both arrays, as many times as they appear in both.

#Walk through both arrays if elements match Add to result
#When they don’t match, move the pointer of the smaller element forward.
#Repeat until one of the arrays ends.
