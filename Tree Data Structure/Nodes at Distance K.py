"""
Given the root of a binary tree A, the value of a target node B, and an integer C, return an array of the values of all nodes that have a distance C from the target node.

You can return the answer in any order.


Problem Constraints
1 ≤ N ≤ 105 (N is the number of nodes in the binary tree)
1 ≤ Ai ≤ N (Ai denotes the values of the nodes in the tree)
All the values in the nodes are unique.
1 ≤ C ≤ 104


Input Format
The first argument is the root node of the binary tree A.
The second argument is an integer B denoting the label of the target node.
The third argument is an integer C denoting the distance.


Output Format
Return an array of integers denoting the nodes which are at a distance C from the node B.
"""

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
from collections import deque


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return a list of integers
    def distanceK(self, A, B, C):
        par = dict()
        par[A] = None
        stack = [A]
        l = 0
        while stack:
            n = stack.pop()
            l += 1
            if n.val == B:
                target = n
            if n.left != None:
                stack.append(n.left)
                par[n.left] = n
            if n.right != None:
                stack.append(n.right)
                par[n.right] = n

        visited = [0 for i in range(l + 1)]
        visited[0] = 1
        q = deque()
        q.append((target, 0))
        ans = []

        while q:
            n, k = q.popleft()
            visited[n.val] = 1
            if k == C:
                ans.append(n.val)
            if k > C:
                continue
            if n.left != None and visited[n.left.val] == 0:
                q.append((n.left, k + 1))
            if n.right != None and visited[n.right.val] == 0:
                q.append((n.right, k + 1))
            if par[n] != None and visited[par[n].val] == 0:
                q.append((par[n], k + 1))

        return ans