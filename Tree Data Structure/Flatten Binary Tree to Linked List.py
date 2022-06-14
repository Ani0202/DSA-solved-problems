"""
Given a binary tree, flatten it to a linked list in-place.
"""


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def flatten(self, A):
        node = A
        while node:
            if node.left:
                n = node.left
                while n.right:
                    n = n.right
                n.right = node.right
                node.right = node.left
                node.left = None
            node = node.right

        return A
