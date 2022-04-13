'''
Problem Description
 
 

You are given the root of a complete binary tree A.

You have to return the value of the rightmost node in the last level of the binary tree.

Try to find a solution with a better time complexity than O(N).



Problem Constraints
1 <= Number of nodes in the binary tree <= 105


Input Format
The first argument is the root of a binary tree A.


Output Format
Return a single integer denoting the value of the rightmost node in the last level of the binary tree.
'''

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def lastNode(self, A):
        h = self.findHeight(A.left)
        if h == 0:
            return A.val
        
        if h == self.findHeight(A.right):
            return self.lastNode(A.right)
        else:
            return self.lastNode(A.left)

    def findHeight(self, node):
        c = 0
        while node:
            c += 1
            node = node.left

        return c

