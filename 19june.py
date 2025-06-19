# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper function to build a linked list from a list
def build_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a list
def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Function to remove all duplicates (only unique elements remain)
def deleteDuplicates(head):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    current = head

    while current:
        if current.next and current.val == current.next.val:
            duplicate_val = current.val
            while current and current.val == duplicate_val:
                current = current.next
            prev.next = current
        else:
            prev = current
            current = current.next

    return dummy.next

# Test case
head = build_list([1, 2, 3, 3, 4, 4, 5])
new_head = deleteDuplicates(head)
print(to_list(new_head))  # Output: [1, 2, 5]

#val: the value of the node   next: a pointer to the next node

#build_list(values)
#Builds a linked list from a Python list.
#Example: build_list([1,2,3]) returns the head of the linked list 1 -> 2 -> 3
#2. to_list(head)
#Converts a linked list back to a Python list, to make it easy to print or test.

#deleteDuplicates(head)
#This function:Removes all occurrences of nodes with duplicate values.
#Keeps only values that are completely unique.

#Iterate through the list.If we find duplicates we record that duplicate value.
#Skip all nodes with that duplicate value.
#Connect prev to the next non-duplicate node.
#If current node is unique, move both prev and current forward.

