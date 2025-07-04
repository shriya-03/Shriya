def window(length, offset, lst):
    if length == 0:
        return [[] for _ in range(0, len(lst)+1, offset)]
    
    result = []
    for i in range(0, len(lst) - length + 1, offset):
        result.append(lst[i:i+length])
    return result

print(window(2, 1, [0, 1, 2, 3, 4]))  # [[0,1], [1,2], [2,3], [3,4]]
print(window(2, 2, [0, 1, 2, 3, 4]))  # [[0,1], [2,3]]
print(window(2, 3, [0, 1, 2, 3, 4]))  # [[0,1], [3,4]]
print(window(0, 2, [1, 2, 3, 4]))     # [[], [], []]
print(window(2, 1, []))              # []


#length: how many items in each group
#offset: how far to move forward for the next group

#window(2, 1, [0, 1, 2, 3, 4])
#length = 2 → each window should have 2 numbers.
#offset = 1 → move forward 1 step each time.
#We cut the list like this:
#[0, 1] ← start at index 0
#[1, 2] ← start at index 1
#[2, 3] ← start at index 2
#[3, 4] ← start at index 3
# Output:
#[0, 1], [1, 2], [2, 3], [3, 4]]