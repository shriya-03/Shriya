def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    prev2 = nums[0]  # max money up to house i-2
    prev1 = max(nums[0], nums[1])  # max money up to house i-1
    
    for i in range(2, len(nums)):
        current = max(prev1, prev2 + nums[i])
        prev2 = prev1
        prev1 = current
    
    return prev1

# Example input
nums = [2, 7, 9, 3, 1,5,7]
print("Example: nums =", nums)
print("Answer:", rob(nums)) #19[2+9+1+7]

#idea is to build the solution from smaller subproblems. The main constraint is: cannot rob two adjacent houses.


