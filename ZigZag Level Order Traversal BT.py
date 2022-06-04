'''
Given a binary tree, return the zigzag level order traversal of its nodes’ values. (ie, from left to right, then right to left for the next level and alternate between).
'''

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        currStack = [A]
        nextStack = []
        ans = []
        row = []
        d = 0

        while currStack:
            node = currStack.pop()
            row.append(node.val)
            if d == 0:
                if node.left != None:
                    nextStack.append(node.left)
                if node.right != None:
                    nextStack.append(node.right)

            else:
                if node.right != None:
                    nextStack.append(node.right)
                if node.left != None:
                    nextStack.append(node.left)

            if len(currStack) == 0:
                ans.append(row)
                row = []
                currStack, nextStack = nextStack, currStack
                d = (d+1)%2

        return ans