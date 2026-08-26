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
    # doing iteratively
    # keep track of previous and current nodes
    previous_node = None
    current_node = head
    while current_node is not None:
        # 1. Save where current is going.
        next_node = current_node.next
        # 2. Reverse current's pointer toward previous.
        current_node.next = previous_node
        # 3. Move previous to current.
        previous_node = current_node
        # 4. Move current to the saved next.
        current_node = next_node
    # return the reversed linked list
    return previous_node

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
