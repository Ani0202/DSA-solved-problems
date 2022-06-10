'''
Problem Description
 
 

You are given the root of a binary tree A, you need to return the absolute difference between sum of all covered elements and the sum of all uncovered 
elements.

In a binary tree, a node is called Uncovered if it appears either on left boundary or right boundary. Rest of the nodes are called covered.



Problem Constraints
1 <= Number of nodes in the binary tree <= 105


Input Format
The first argument is the root of the binary tree A.


Output Format
Return a single integer denoting the absolute difference of the sum of covered and uncovered nodes.
'''

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
     # @return an long
    def coveredNodes(self, A):
        sum1 = 0
        sum2 = 0
        q = list()
        q.append(A)
        cs = 0
        us = 0
        while len(q):
            n = len(q)
            i = 0
            while i < n:
                node = q.pop(0)
                if i == 0:
                    us += node.val
                elif i == n-1:
                    us += node.val
                else:
                    cs += node.val

                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)

                i += 1

        return abs(cs-us)

                
