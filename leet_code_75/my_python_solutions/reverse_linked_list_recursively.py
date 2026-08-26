# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# Input: head = [1,2]
# Output: [2,1]

# Example 3:

# Input: head = []
# Output: []

# Constraints:
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    # base cases
    # case 1: we are not at a valid node
    if head is None:
        return None
    # case 2: we are at the tail
    elif head.next is None:
        return head
    # case 3: we are anywhere but the tail
    else:
        # get the current node
        current_node = head
        # set the new head to the last valid node of the linked list, using recursion
        new_head = reverseList(current_node.next)
        # Connect the tail of the reversed portion to the current node.
        (current_node.next).next = current_node
        # Break the current node's old forward link to prevent a cycle
        current_node.next = None
        # return the head of the reversed linked list
        return new_head

# Helper functions to run tests
def build_list(values):
    head = None
    current = None
    for value in values:
        new_node = ListNode(value)
        if head is None:
            head = new_node
        else:
            current.next = new_node
        current = new_node
    return head
def to_array(head):
    result = []
    while head is not None:
        result.append(head.val)
        head = head.next
    return result

# Test cases
test_cases = [
    [1, 2, 3, 4, 5],
    [1, 2],
    [],
    [1, 2, 3, 4]
                    ]
# run my tests
for values in test_cases:
    head = build_list(values)

    print("Original: ", to_array(head))

    reversed_head = reverseList(head)

    print("Reversed: ", to_array(reversed_head), "\n")
