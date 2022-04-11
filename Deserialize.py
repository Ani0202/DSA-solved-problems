'''
Problem Description
 
 

You are given a string A which is a serialized string. You have to restore the original array of strings.

The string in the output array should only have lowercase english alphabets.

Serialization: Scan each element in a string, calculate its length and append it with a string and a element separator or deliminator (the deliminator is ~). We append the length of the string so that we know the length of each element.

For example, for a string 'interviewbit', its serialized version would be 'interviewbit12~'.



Problem Constraints
1 <= |A| <= 106


Input Format
The first argument is the string A.


Output Format
Return an array of strings which are deserialized.
'''

class Solution:
    # @param A : string
    # @return a list of strings
    def deserialize(self, A):
        ans = []
        i = 0
        while i < len(A):
            if 57 >= ord(A[i]) >= 48:
                s = ''
                j = i
                while A[j] != '~':
                    s += A[j]
                    j += 1

                s = int(s)
                ans.append(A[i-s:i])
                i = j+1

            else:
                i += 1

        return ans