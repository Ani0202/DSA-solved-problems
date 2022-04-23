'''
Given 2 integers A and B and an array of integars C of size N.

Element C[i] represents length of ith board.

You have to paint all N boards [C0, C1, C2, C3 … CN-1]. There are A painters available and each of them takes B units of time to paint 1 unit of 
board.

Calculate and return minimum time required to paint all boards under the constraints that any painter will only paint contiguous sections of 
board.

2 painters cannot share a board to paint. That is to say, a board
cannot be painted partially by one painter, and partially by another.
A painter will only paint contiguous boards. Which means a
configuration where painter 1 paints board 1 and 3 but not 2 is
invalid.
Return the ans % 10000003




Input Format

The first argument given is the integer A.
The second argument given is the integer B.
The third argument given is the integer array C.
Output Format

Return minimum time required to paint all boards under the constraints that any painter will only paint contiguous sections of board % 10000003.
Constraints

1 <=A <= 1000
1 <= B <= 10^6
1 <= C.size() <= 10^5
1 <= C[i] <= 10^6
'''

class Solution:
	# @param A : integer
	# @param B : integer
	# @param C : list of integers
	# @return an integer
	def paint(self, A, B, C):
        l = max(C)
        h = sum(C)
        ans = float('inf')

        def noOfPainters(mid):
            painters = 1
            total = 0
            for i in C:
                total += i
                if total > mid:
                    total = i
                    painters += 1
                    if painters > A:
                        return painters
                    
            return painters
        while l <= h:
            m = l + (h-l)//2
            n = noOfPainters(m)
            if n <= A:
                ans = m
                h = m-1
            else:
                l = m+1

        return (ans*B)%10000003
