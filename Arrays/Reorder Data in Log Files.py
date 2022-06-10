'''
You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.

Reorder these logs so that:

The letter-logs come before all digit-logs.
The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
The digit-logs maintain their relative ordering.

Return the final order of the logs.


Problem Constraints
1 <= logs.length <= 1000
3 <= logs[i].length <= 1000
All the tokens of logs[i] are separated by a single space.
logs[i] is guaranteed to have an identifier and at least one word after the identifier.


Input Format
The first argument is a string array A where each element is a log.


Output Format
Return the string array A after making the changes.
'''

class Solution:
    # @param A : list of strings
    # @return a list of strings
    def reorderLogs(self, A):
        letters = []
        digits = []
        for log in A:
            word = log.split('-')
            if word[1].isdigit():
                digits.append(log)
            else:
                letters.append((word[0], '-'.join(word[1:])))
        letters = sorted(letters, key = lambda x: (x[1], x[0]))
        letters = ['-'.join(l) for l in letters]

        return letters+digits