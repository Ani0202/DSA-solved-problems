'''
Problem Description
 
 

Given N x N matrix filled with 0, 1, 2, 3.

Find whether there is a path possible from source to destination, traversing through blank cells only. 
 
You can traverse up, down, right, and left. Return a single integer 1 if a path exists, otherwise 0.

A value of cell 1 means Source.
A value of cell 2 means Destination.
A value of cell 3 means Blank cell.
A value of cell 0 means Blank Wall.
Note: there are an only a single source and single destination(sink).


Problem Constraints
2 <= N <= 103
0 <= Ai, j <= 3


Input Format
The first argument is the 2D integer array A.


Output Format
Return a single integer 1 if a path exists, otherwise 0.
'''

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def checkPath(self, A):
        N = len(A)
        visited = [[0 for i in range(N)] for j in range(N)]

        def findSource():
            for i in range(N):
                for j in range(N):
                    if A[i][j] == 1:
                        return (i,j)

        x,y = findSource()
        visited[x][y] = 1

        stack = [(x,y)]
        while len(stack):
            i, j = stack.pop()
            if i-1 >= 0 and visited[i-1][j] == 0:
                visited[i-1][j] = 1
                if A[i-1][j] == 2:
                    return 1
                elif A[i-1][j] == 3:
                    stack.append((i-1, j))

            if j+1 < N and visited[i][j+1] == 0:
                visited[i][j+1] = 1
                if A[i][j+1] == 2:
                    return 1
                elif A[i][j+1] == 3:
                    stack.append((i, j+1))

            if i+1 < N and visited[i+1][j] == 0:
                visited[i+1][j] = 1
                if A[i+1][j] == 2:
                    return 1
                elif A[i+1][j] == 3:
                    stack.append((i+1, j))

            if j-1 >= 0 and visited[i][j-1] == 0:
                visited[i][j-1] = 1
                if A[i][j-1] == 2:
                    return 1
                elif A[i][j-1] == 3:
                    stack.append((i, j-1))

        return 0
