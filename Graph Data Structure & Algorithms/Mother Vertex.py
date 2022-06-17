"""
You are given a directed graph with A vertices and M edges.

You are given an array B with dimensions M x 2, where each row denotes a directed edge from Bi, 0 to Bi, 1.

You need to find if there exists a mother vertex in the given graph. Return 1 if it exists, otherwise 0.

A mother vertex is defined as a vertex from which all the vertices in the graph are accessible by a directed path.



Problem Constraints
1 <= A <= 105
1 <= M <= 2 * 105
1 <= Bi, 0, Bi, 1 <= A
There can be duplicate edges or self loops in the input graph.


Input Format
The first argument is the integer A. The second argument is the 2D integer array B.


Output Format
Return a single integer 1 if a mother vertex exists, otherwise 0.
"""

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def motherVertex(self, A, B):
        graph = [[] for i in range(A + 1)]
        for i, j in B:
            graph[i].append(j)

        def dfs(a):
            stack = [a]
            while stack:
                n = stack.pop()
                visited[n] = 1

                for child in graph[n]:
                    if visited[child] == 0:
                        stack.append(child)
                        visited[child] = 1

        visited = [0 for i in range(A + 1)]
        res = None
        for i in range(1, A + 1):
            if visited[i] == 0:
                res = i
                dfs(i)

        visited = [0 for i in range(A + 1)]
        dfs(res)

        for i in range(1, A + 1):
            if visited[i] == 0:
                return 0

        return 1
