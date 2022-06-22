"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses of length 2*n.
"""


class Solution:
    # @param A : integer
    # @return a list of strings
    def generateParenthesis(self, A):
        s = '(' * A + ')' * A
        temp = ''
        ans = []
        self.findPar(s, temp, ans, 0)
        return ans

    def findPar(self, s, temp, ans, start):
        if s == '':
            ans.append(temp[:])
            return

        for i in range(len(s)):
            if i != 0 and s[i] == s[i - 1]:
                continue

            if s[i] == ')' and start <= 0:
                continue

            temp += s[i]
            if s[i] == '(':
                self.findPar(s[:i] + s[i + 1:], temp, ans, start + 1)
            else:
                self.findPar(s[:i] + s[i + 1:], temp, ans, start - 1)

            temp = temp[:-1]
