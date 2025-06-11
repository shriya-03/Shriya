def merge_two_sorted_arrays(arr1, arr2):
    i = j = 0
    merged = []
    
    # Traverse both arrays and append the smaller element.
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    
    # Append remaining elements (only one of these loops will execute).
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
    
    return merged

# Example usage:
print(merge_two_sorted_arrays([1, 3, 5], [2, 4, 6]))  # Output: [1, 2, 3, 4, 5, 6]

#Two-Pointer Technique: Two pointers, i and j, traverse arr1 and arr2 respectively. 
# The smaller element is appended to the merged list.

#Handling Remaining Elements: After one array is fully processed, the remaining 
# elements of the other array are appended.