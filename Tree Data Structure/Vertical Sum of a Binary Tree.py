'''
Problem Description
 
 

You are given the root of a binary tree A.

You have to find the vertical sum of the tree.

A vertical sum denotes an array of sum of the different verticals of a binary tree,

where the leftmost vertical sum is the first element of the array and rightmost vertical is the last.



Problem Constraints
1 <= Number of nodes in the binary tree <= 105
1 <= Ai <= 103


Input Format
The first argument is the root of a binary tree A.


Output Format
Return an array denoting the vertical sum of the binary tree.
'''

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def verticalSum(self, A):
        vertiSum = dict()
        stack = [(0, A)]
        while len(stack):
            pos, node = stack.pop()
            vertiSum[pos] = vertiSum.get(pos, 0) + node.val
            if node.left != None:
                stack.append((pos-1, node.left))
            if node.right != None:
                stack.append((pos+1, node.right))

        ans = []
        for key in sorted(vertiSum):
            ans.append(vertiSum[key])
        return ans