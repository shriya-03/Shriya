def count_positives(arr):
    return sum(1 for x in arr if x > 0)

print(count_positives([3, -1, 0, 5, -2,]))  # Output: 2

#The function takes in an argument arr, which is expected to be a list
#The sum() function:
#The sum() function is used here to add up a series of values. It sums the result of a
#  generator expression that produces 1 for each positive number in arr.

#The Generator Expression (1 for x in arr if x > 0):
#This is a loop that iterates over the list arr.
#x for x in arr: This is the loop part that iterates over each element x in the list arr.
#if x > 0: This condition ensures that only the positive numbers (greater than 0) are counted.
#For each positive x, the generator yields the value 1.

#The sum() function then adds up all the 1s that were generated. In other words, it counts how many 
# times the condition x > 0 is true.
