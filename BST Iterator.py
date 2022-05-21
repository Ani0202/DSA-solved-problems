'''
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

The first call to next() will return the smallest number in BST. Calling next() again will return the next smallest number in the BST, and so on.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.root = root
        self.stack = []
        node = self.root
        while node:
            self.stack.append(node)
            node = node.left
        

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if len(self.stack) != 0:
            return True
        else:
            return False
        

    # @return an integer, the next smallest number
    def next(self):
        node = self.stack.pop()
        if node.right != None:
            right = node.right
            while right:
                self.stack.append(right)
                right = right.left

        return node.val
        

# Your BSTIterator will be called like this:
# i = BSTIterator(root)
# while i.hasNext(): print i.next(),
