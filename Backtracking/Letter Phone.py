"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



The digit 0 maps to 0 itself.

The digit 1 maps to 1 itself.
"""


class Solution:
    # @param A : string
    # @return a list of strings
    def __init__(self):
        self.hmap = {'0': '0', '1': '1', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs',
                     '8': 'tuv', '9': 'wxyz'}

    def letterCombinations(self, A):

        ans = []
        temp = ''
        self.findComb(A, 0, temp, ans)
        return ans

    def findComb(self, A, i, temp, ans):
        if len(temp) == len(A):
            ans.append(temp[:])
            return

        for j in self.hmap[A[i]]:
            temp += j
            self.findComb(A, i + 1, temp, ans)
            temp = temp[:-1]
