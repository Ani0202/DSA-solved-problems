'''
You rolled a dice K times and got a sum of A after summing all the values you got after a roll.
Find the number of ways you could have got a sum of A after rolling K times, since this value can be very large return modulo 109+7.


Problem Constraints
1 <= A <= 106


Input Format
Given an integer A.


Output Format
Return and integer.
'''

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        mod = int(1e9 + 7)
        if 1 <= A <= 6:
            return (1 << (A-1))

        dp = [0] * (A+1)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        dp[4] = 8
        dp[5] = 16
        dp[6] = 32

        if 1 <= A <= 6:
            return dp[A]
        
        for i in range(1, A+1):
            if 1 <= i <= 6:
                dp[i] = (1 << i-1)
            else:
                dp[i] = (dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4] + dp[i-5] + dp[i-6]) % mod
        
        # print(dp)
        ans =  dp[-1] % mod
        return ans