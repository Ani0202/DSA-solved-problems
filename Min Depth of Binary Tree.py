'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

NOTE : The path has to end on a leaf node.
'''

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None
from collections import deque

class Solution:
	# @param A : root node of tree
	# @return an integer
	def minDepth(self, A):
        q = deque()
        q.append((A, 1))
        while len(q):
            node, d = q.popleft()
            if node.left == None and node.right == None:
                return d
            if node.left != None:
                q.append((node.left, d+1))
            if node.right != None:
                q.append((node.right, d+1))

        