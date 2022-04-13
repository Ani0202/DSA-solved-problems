'''
Problem Description
 
 

You are given the root of a binary tree A.
You have to find out the number of parent - child relationship whose values are consecutive numbers.



Problem Constraints
1 <= Number of nodes in the tree <= 105


Input Format
The first argument is the root of the binary tree A.


Output Format
Return a single integer denoting the number of consecutive parent - child relationships.
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
    def consecutiveNodes(self, A):
        ans = 0
        stack = [(-1, A)]
        while len(stack):
            par, node = stack.pop()
            if abs(par - node.val) == 1:
                ans += 1
            if node.left != None:
                stack.append((node.val, node.left))
            if node.right != None:
                stack.append((node.val, node.right))

        return ans