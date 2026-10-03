class Solution:
    def climbStairs(self, N: int) -> int:
        if N == 1:
            return 1

        dp = [1, 2]

        for i in range(2, N):
            cur = dp[0] + dp[1]
            dp[0], dp[1] = dp[1], cur
        
        return dp[-1]