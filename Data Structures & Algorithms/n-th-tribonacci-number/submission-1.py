class Solution:
    def tribonacci(self, N: int) -> int:
        if N <= 2:
            return 0 if N == 0 else 1 
        dp = [0] * (N + 1)
        dp[0], dp[1], dp[2] = 0, 1, 1

        for i in range(3, N+1):
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
        
        return dp[-1]
