"""
Given a string A consisting of lowercase characters.

We need to tell minimum characters to be appended (insertion at end) to make the string A a palindrome.



Problem Constraints
1 <= |A| <= 105

A consists only of lower-case characters.



Input Format
First argument is an string A.



Output Format
Return a integer denoting the minimum characters to be appended (insertion at end) to make the string A a palindrome.
"""


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        s = A[::-1] + '.' + A
        l = 0
        i = 1
        n = len(s)
        lps = [0 for i in range(n)]
        while i < n:
            if s[i] == s[l]:
                l += 1
                lps[i] = l
                i += 1
            else:
                if l != 0:
                    l = lps[l - 1]
                else:
                    lps[i] = 0
                    i += 1

        return len(A) - lps[-1]
