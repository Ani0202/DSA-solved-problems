"""
Given a stream of numbers A. On arrival of each number, you need to increase its first occurence by 1 and include this in the stream.

Return the final stream of numbers.



Problem Constraints
1 <= |A| <= 100000

1 <= A[i] <= 10000



Input Format
First and only argument is the array A.



Output Format
Return an array, the final stream of numbers.
"""


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        d = dict()

        for i in range(len(A)):
            if A[i] in d:
                A[d[A[i]]] += 1
                if A[d[A[i]]] in d:
                    if d[A[d[A[i]]]] > d[A[i]]:
                        d[A[d[A[i]]]] = d[A[i]]
                else:
                    d[A[d[A[i]]]] = d[A[i]]

            d[A[i]] = i

        return A

