"""
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
"""


# Definition for a  binary tree node
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        par = root
        while par:
            node = par
            startNode = None
            prevNode = None
            while node:
                if node.left:
                    if startNode is None:
                        startNode = node.left
                        prevNode = node.left
                    else:
                        prevNode.next = node.left
                        prevNode = node.left

                if node.right:
                    if startNode is None:
                        startNode = node.right
                        prevNode = node.right
                    else:
                        prevNode.next = node.right
                        prevNode = node.right

                node = node.next
            par = startNode
