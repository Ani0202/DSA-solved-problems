'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note: You may assume that duplicates do not exist in the tree.
'''

class Solution:
    def buildTree(self, preorder, inorder):
        if not inorder:
            return None
            
        root_value = preorder[0]
        root_index = inorder.index(root_value)
        
        left_nodes = inorder[:root_index]
        right_nodes = inorder[root_index+1 : ]
        
        m, n = len(left_nodes), len(right_nodes)
        
        root = TreeNode(root_value)
        root.left = self.buildTree(preorder[1 : m+1], left_nodes)
        root.right = self.buildTree(preorder[m+1:], right_nodes)
        
        return root