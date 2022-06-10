'''
Problem Description

Given a binary tree, return the reverse level order traversal of its nodes values. (i.e, from left to right and from last level to starting level).



Problem Constraints
1 <= number of nodes <= 5 * 105

1 <= node value <= 105



Input Format
First and only argument is a pointer to the root node of the Binary Tree, A.



Output Format
Return an integer array denoting the reverse level order traversal from left to right.
'''

from collections import deque

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, root):
        S = [] 
        Q = deque() 
        Q.append(root)
        while(len(Q) > 0 ): 
      
            # Dequeue node and make it root 
            root = Q.popleft()
            S.append(root.val) 
      
            # Enqueue right child 
            if (root.right): 
                Q.append(root.right) 
      
            # Enqueue left child 
            if (root.left): 
                Q.append(root.left) 
      
        return reversed(S)   