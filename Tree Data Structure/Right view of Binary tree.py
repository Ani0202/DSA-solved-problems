'''
Given a binary tree A of integers. Return an array of integers representing the right view of the Binary tree.

Right view of a Binary Tree: is a set of nodes visible when the tree is visited from Right side.



Problem Constraints
1 <= Number of nodes in binary tree <= 105

0 <= node values <= 109 



Input Format
First and only argument is an pointer to the root of binary tree A.



Output Format
Return an integer array denoting the right view of the binary tree A.
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        ans = []
        stack = [A]
        while stack:
            ans.append(stack[-1].val)
            stack2 = []
            for node in stack:
                if node.left:
                    stack2.append(node.left)
                if node.right:
                    stack2.append(node.right)

            stack = stack2

        return ans