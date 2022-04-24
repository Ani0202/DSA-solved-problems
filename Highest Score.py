'''
Problem Description
 
 

You are given a 2D string array A of dimensions N x 2,

where each row consists of two strings: first is the name of the student, second is their marks.

You have to find the maximum average mark. If it is a floating point, round it down to the nearest integer less than or equal to the number.



Problem Constraints
1 <= N <= 105


Input Format
The first argument is a 2D string array A.


Output Format
Return a single integer which is the highest average mark.
'''

class Solution:
    # @param A : list of list of strings
    # @return an integer
    def highestScore(self, A):
        marks = dict()
        for l in A:
            if l[0] in marks:
                marks[l[0]].append(int(l[1]))
            else:
                marks[l[0]] = [int(l[1])]

        avg = []
        for k,v in marks.items():
            avg.append(sum(v)//len(v))

        return max(avg)
