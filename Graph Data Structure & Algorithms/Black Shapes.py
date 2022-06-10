"""
Given N x M character matrix A of O's and X's, where O = white, X = black.


Return the number of black shapes. A black shape consists of one or more adjacent X's (diagonals not included)




Input Format:

    The First and only argument is a N x M character matrix.
Output Format:

    Return a single integer denoting number of black shapes.
Constraints:

    1 <= N,M <= 1000
    A[i][j] = 'X' or 'O'
"""


class Solution:
    # @param A : list of strings
    # @return an integer
    def __init__(self):
        self.dx = [1, -1, 0, 0]
        self.dy = [0, 0, 1, -1]

    def black(self, A):
        n = len(A)
        m = len(A[0])
        visited = [[False] * m for _ in range(n)]
        ans = 0

        for i in range(n):
            for j in range(m):
                if (not visited[i][j]) and A[i][j] == "X":
                    self.solve(i, j, n, m, visited, A)
                    ans += 1
        return ans

    def solve(self, x, y, n, m, visited, A):
        if visited[x][y] or A[x][y] != "X":
            return
        visited[x][y] = True
        for i in range(4):
            newx = x + self.dx[i]
            newy = y + self.dy[i]
            if 0 <= newx < n and 0 <= newy < m and visited[newx][newy] == False:
                self.solve(newx, newy, n, m, visited, A)
