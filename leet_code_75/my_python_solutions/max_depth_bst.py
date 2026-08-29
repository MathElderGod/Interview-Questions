# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:
# Input: root = [1,null,2]
# Output: 2

# Constraints:
# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    # return 0 if the root is null
    if root is None:
        return 0
    # return the max height between the left and right subtrees + 1
    return max(maxDepth(root.left), maxDepth(root.right)) + 1

# Test 1
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

print(maxDepth(root1))  # Expected: 3


# Test 2
root2 = TreeNode(1)
root2.right = TreeNode(2)

print(maxDepth(root2))  # Expected: 2


# Test 3
root3 = TreeNode(8)
root3.left = TreeNode(3)
root3.right = TreeNode(10)
root3.left.left = TreeNode(1)
root3.left.right = TreeNode(6)
root3.left.right.left = TreeNode(4)
root3.left.right.right = TreeNode(7)

print(maxDepth(root3))  # Expected: 4
