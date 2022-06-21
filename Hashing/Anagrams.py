"""
Given an array of strings, return all groups of strings that are anagrams. Represent a group by a list of integers representing the index in the original list. Look at the sample case for clarification.

Anagram : a word, phrase, or name formed by rearranging the letters of another, such as 'spar', formed from 'rasp'

Note:  All inputs will be in lower-case.

Example :

Input : cat dog god tca
Output : [[1, 4], [2, 3]]
"""


class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        count = dict()

        for i in range(len(A)):
            t = sorted(A[i])
            n = ''.join(t)
            if n in count:
                count[n].append(i + 1)
            else:
                count[n] = [i + 1]

        ans = []
        for v in count.values():
            ans.append(v)
        return ans
