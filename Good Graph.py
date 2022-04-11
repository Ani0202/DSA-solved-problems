'''
Given a directed graph of N nodes where each node is pointing to any one of the N nodes (can possibly point to itself). Ishu, the coder, is bored 
and he has discovered a problem out of it to keep himself busy. Problem is as follows:

A node is 'good'if it satisfies one of the following:

1. It is the special node (marked as node 1)
2. It is pointing to the special node (node 1)
3. It is pointing to a good node.
Ishu is going to change pointers of some nodes to make them all ‘good’. You have to find the min. number of pointers to change in order to

make all the nodes good (Thus, a Good Graph).

Note: Resultant Graph should hold the property that all nodes are good and each node must point to exactly one node.

Constraints:

1 <= N <= 100,000
Input:

A vector of N integers containing N numbers all between 1 to N, where i-th number is the number of node that i-th node is pointing to.
Output:

An Integer denoting min. number of pointer changes.
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, a):
        n = len(a)
        self.g = [[] for _ in range(n+1)]
        self.visited = [False]*(n+1)
        self.good = [False]*(n+1)
        self.good[1] = True
        self.ans = 0
        for i in range(n):
            self.g[i+1].append(a[i])
        for i in range(1, n+1):
            if self.visited[i]==False and self.good[i]==False:
                self.dfs(i)
        return self.ans
    
    def dfs(self, a):
        self.visited[a] = True
        flag = False

        for e in self.g[a]:
            if self.good[e]==True:
                self.good[a] = True
                return
            if self.visited[e]==False:
                flag = True
                self.dfs(e)
        
        if flag==False:
            self.ans += 1
        self.good[a] = True