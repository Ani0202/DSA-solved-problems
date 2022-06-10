'''
There are A people numbered 1 to A in a football academy.

The coach of the academy wants to make two teams (not necessary of equal size) but unfortunately, not all people get along, and several refuse to be put on the same team as that of their enemies.

Given a 2-D array B of size M x 2 denoting the enemies i.e B[i][0] and B[i][1] both are enemies of each other.

Return 1 if it possible to make exactly two teams else return 0.



Problem Constraints
2 <= A <= 105

1 <= M <= 105

1 <= B[i][0], B[i][1] <= A

B[i][0] != B[i][1]



Input Format
First argument is an integer A denoting number of peoples.

Second argument is a 2-D array B of size M x 2 denoting enemies.



Output Format
Return 1 if it possible to make exactly two teams else return 0.
'''

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        teams = [-1 for i in range(A+1)]
        enemies = [[] for i in range(A+1)]
        for enemy in B:
            enemies[enemy[0]].append(enemy[1])
            enemies[enemy[1]].append(enemy[0])

        def makeTeam(node):
            queue = [node]
            while queue:
                x = queue.pop()
                for y in enemies[x]:
                    if teams[y] == -1:
                        teams[y] = 1 - teams[x]
                        queue.append(y)
                    elif teams[y] == teams[x]:
                        return 0

            return 1

        for i in range(1, A+1):
            if teams[i] == -1:
                if not makeTeam(i):
                    return 0

        return 1
