'''
You are given a array of strings A of length N.


You have to return another string array which contains all possible special strings.

A special string is defined as a string with length equal to N, 

and ith character of the string is equal to any character of the ith string in the array A.



Problem Constraints
1 <= N <= 5
1 <= |Ai| <= 8


Input Format
The first argument is the string array A.


Output Format
Return a string array consisting of all possible special strings.
'''

class Solution:
    # @param A : list of strings
    # @return a list of strings
    def specialStrings(self, A):
        n = len(A)
        temp = ""
        ans = []
        return self.findSpecialStrings(A, n, temp, ans, 0)

    def findSpecialStrings(self, A, n, temp, ans, idx):
        if len(temp) == n:
            ans.append(temp[:])
            return ans

        for j in range(len(A[idx])):
            temp += A[idx][j]
            self.findSpecialStrings(A, n, temp, ans, idx+1)
            temp = temp[:-1]

        return ans