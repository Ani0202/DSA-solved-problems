'''
Given an undirected tree with an even number of nodes. Consider each connection between a parent and child node to be an edge.

You need to remove maximum number of these edges, such that the disconnected subtrees that remain each have an even number of nodes.

Return the maximum number of edges you can remove.



Problem Constraints
2 <= A <= 105

1 <= B[i][0], B[i][1] <= A

Integer A will be even.



Input Format
First argument is an integer A denoting the number of nodes in the tree.

Second argument is a 2D array B of size (A-1) * 2, denoting the edge between nodes B[i][0] and B[i][1].



Output Format
Return an integer, denoting the maximum number of edges you can remove.
'''
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        edges = [[] for i in range(A+1)]
        self.ans = 0
        for edge in B:
            edges[edge[0]].append(edge[1])
            edges[edge[1]].append(edge[0])

        

        def dfs(node, par):
            currNodes = 0
            for child in edges[node]:
                if child == par:
                    continue
            
                subTreeCount = dfs(child, node)

                if subTreeCount % 2 == 0:
                    self.ans += 1
                else:
                    currNodes += subTreeCount

            return currNodes + 1

        dfs(1, 0)
        return self.ans
