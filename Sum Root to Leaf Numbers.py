'''
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers % 1003.
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
    def sumNumbers(self, A):
        temp = 0
        return self.findSum(temp, A) % 1003

    def findSum(self, temp, node):
        if node.left == None and node.right == None:
            return (temp*10 + node.val) % 1003
        l = 0
        r = 0
        temp = temp*10 + node.val
        temp %= 1003
        if node.left != None:
            l = self.findSum(temp, node.left)
        if node.right != None:
            r = self.findSum(temp, node.right)

        return (l + r)%1003