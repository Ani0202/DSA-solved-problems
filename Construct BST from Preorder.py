'''
Problem Description
 
 

Given an integer array A with distinct elements, which represents the preorder traversal of a binary search tree,
 
construct the tree and return its root.

A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.

A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.



**Problem Constraints**
1 <= |A| <= 105
1 <= A.val <= 109
The given array is a valid preorder traversal of a BST.


**Input Format**
The first argument is an integer array denoting the preorder traversal.


**Output Format**
Return the root of the Binary Search Tree.
'''

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
sys.setrecursionlimit(200000)

class Solution:
    def constructBST(self, A):        
        self.idx = 0
        n = len(A)        
        return self.helper(float('-inf'), float('inf'), n, A)

    def helper(self, lower, upper, n, A):
        if self.idx == n:
            return None
        val = A[self.idx]
        if val < lower or val > upper:
            return None
        self.idx += 1
        root = TreeNode(val)
        root.left = self.helper(lower, val, n, A)
        root.right = self.helper(val, upper, n, A)
        return root