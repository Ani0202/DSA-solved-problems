'''
Problem Description
 
 

You are given an assignment to sort out the files of your department today.

A file contains various records. Each record has an (ID, Parent ID).

To make your task easier, you decided to separate records into different sets.

If a set contains a record with (ID, Parent ID) - (X, Y), then both X and Y must be present in the set.

There are A records. You are also given a 2D array B of dimensions N x 2,

where each row is record's (ID, Parent ID).



You have to find the maximum number of sets you can divide the records into.



Problem Constraints
1 <= A, N <= 105
1 <= B[i][0], B[i][1] <= A
There can be duplicate records.
There can be two records (X, Y) and (Y, X).


Input Format
The first argument is the integer A.
The second argument is the 2D integer array B.


Output Format
Return a single integer denoting the maximum number of sets you can break the record into.
'''

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def breakRecords(self, A, B):
        graph = [[] for i in range(A+1)]
        for edge in B:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        visited = [0 for i in range(A+1)]
        ans = 0
        for i in range(1, A+1):
            if visited[i] == 0:
                stack = [i]
                visited[i] = 1
                while len(stack):
                    node = stack.pop()
                    for child in graph[node]:
                        if visited[child] == 0:
                            visited[child] = 1
                            stack.append(child)

                ans += 1

        return ans