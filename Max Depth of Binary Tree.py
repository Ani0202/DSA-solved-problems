# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return an integer
	def maxDepth(self, A):

        stack = []
        ans = 1
        stack.append((A, 1))
        while len(stack) > 0:
            node, l = stack.pop()
            if node:
                ans = max(ans, l)
                if node.left:
                    stack.append((node.left, l+1))
                if node.right:
                    stack.append((node.right, l+1))

        return ans
