"""
You are travelling to Neverland. After a long journey, you decided to take rest in a hotel for a night.

You have the map of Neverland in the form of 2D matrix A with dimensions N x M.

The rows are numbered from 1 to N, and the columns are numbered from 1 to M.

You can travel from one cell to any adjacent cell. Two cells are considered adjacent if they share a side.

In the map, there are only two digits, 0 and 1,
where 1 denotes a hotel in that cell, and 0 denotes an empty cell.

You are also given another 2D array B with dimension Q x 2,

where each row denotes a co-ordinate (X, Y) on the map (1 - indexed).
For each coordinate you have to find the distance to the nearest hotel.

Return an array denoting the answer to each coordinate in the array B.



**Problem Constraints**
1 <= N, M <= 103
1 <= Q <= 105
0 <= A[i][j] <= 1
0 <= B[i][0] < N
0 <= B[i][1] < M
There is guranteed to be atleast one hotel on the map.


**Input Format**
The first argument is the 2D integer array A.
The second argument is the 2D integer array B.


**Output Format**
Return an integer array denoting the answer to each coordinate in the array B.
"""
from collections import deque


class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def nearestHotel(self, A, B):
        n = len(A)
        m = len(A[0])
        q = deque()
        mp = [[0 for i in range(m + 1)] for j in range(n + 1)]

        for i in range(n):
            for j in range(m):
                if A[i][j] == 0:
                    mp[i + 1][j + 1] = -1
                else:
                    q.append((i + 1, j + 1))

        xd = [0, -1, 0, 1]
        yd = [1, 0, -1, 0]
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + xd[i]
                ny = y + yd[i]
                if 0 < nx <= n and 0 < ny <= m and mp[nx][ny] == -1:
                    mp[nx][ny] = mp[x][y] + 1
                    q.append((nx, ny))

        res = []
        for i in range(len(B)):
            res.append(mp[B[i][0]][B[i][1]])

        return res
