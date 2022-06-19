"""
Given an inorder traversal of a cartesian tree, construct the tree.

Cartesian tree :  is a heap ordered binary tree, where the root is greater than all the elements in the subtree.

Note: You may assume that duplicates do not exist in the tree.
"""


# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    def buildTree(self, A):
        start = 0
        end = len(A) - 1
        return self.constTree(A, start, end)

    def constTree(self, A, s, e):
        if s > e:
            return
        idx = s
        for i in range(s, e + 1):
            if A[i] > A[idx]:
                idx = i

        root = TreeNode(A[idx])
        root.left = self.constTree(A, s, idx - 1)
        root.right = self.constTree(A, idx + 1, e)

        return root
