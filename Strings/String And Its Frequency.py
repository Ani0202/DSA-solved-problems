'''
Problem Description
 
 

 Given a string A with lowercase english alphabets and you have to return a string in which, with each character its frequency is written in adjacent.



Problem Constraints
1 <= |A| <= 105


Input Format
First argument is the string A with lowercase english alphabets.


Output Format
Return a string in which each character frequency is written in adjacent.
'''

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        count = dict()
        for i in A:
            count[i] = count.get(i, 0) + 1

        ans = ''
        for i in A:
            if count[i] != 0:
                ans += i+str(count[i])
            count[i] = 0

        return ans