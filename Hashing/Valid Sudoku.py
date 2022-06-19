"""
Determine if a Sudoku is valid, according to: http://sudoku.com.au/TheRules.aspx

The Sudoku board could be partially filled, where empty cells are filled with the character ‘.’.
"""

class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
        n = 9

        def isPoss(n):
            hmap = dict()
            for i in n:
                if i != '.':
                    if i in hmap:
                        return 0
                    else:
                        hmap[i] = 1

            return 1

        for i in range(n):
            if not isPoss(A[i]):
                return 0

        for j in range(n):
            t = ''
            for i in range(n):
                t += A[i][j]
            if not isPoss(t):
                return 0

        for i in range(0, n, 3):
            for j in range(0, n, 3):
                t = ''
                for k in range(i, i + 3):
                    for m in range(j, j + 3):
                        t += A[k][m]
                if not isPoss(t):
                    return 0

        return 1
