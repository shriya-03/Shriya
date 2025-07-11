def find_lone_no(arr):
    s = set(arr)
    for num in s:
        if -num not in s:
            return num

print(find_lone_no([1, -1, 2, -2, 3]))              # Output: 3
print(find_lone_no([-3, 1, 2, 3, -1, -4, -2]))      # Output: -4
print(find_lone_no([1, -1, 2, -2, 3, 3]))           # Output: 3




# set(arr):
# Removes duplicates and allows fast lookup (O(1)).
# We don't care how many times a number appears — only if its opposite sign exists.
# Loop through each unique number:
# If -num is not in the set, it means no matching opposite exists.
# Return that number.