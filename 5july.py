def compound_array(arr1, arr2):
    result = []
    max_len = max(len(arr1), len(arr2))
    
    for i in range(max_len):
        if i < len(arr1):
            result.append(arr1[i])
        if i < len(arr2):
            result.append(arr2[i])
    
    return result

# Example usage
print(compound_array([1, 2, 3, 4, 5, 6], [9, 8, 7, 6]))
# Output: [1, 9, 2, 8, 3, 7, 4, 6, 5, 6]
