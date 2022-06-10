'''
Given a binary search tree, write a function to find the kth smallest element in the tree.

Example :

Input : 
  2
 / \
1   3

and k = 2

Return : 2

As 2 is the second smallest element in the tree.
NOTE : You may assume 1 <= k <= Total number of nodes in BST
'''

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @return an integer
	def kthsmallest(self, A, B):
        h = self.count(A.left)
        if h == B-1:
            return A.val
        if h < B-1:
            return self.kthsmallest(A.right, B-h-1)
        else:
            return self.kthsmallest(A.left, B)

    def count(self, node):
        queue = [node]
        c = 0
        while len(queue):
            n = queue.pop(0)
            if n != None:
                c += 1
                if n.left != None:
                    queue.append(n.left)
                if n.right != None:
                    queue.append(n.right)

        return c
