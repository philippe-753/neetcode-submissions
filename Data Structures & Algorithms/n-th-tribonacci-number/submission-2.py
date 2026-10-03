class Solution:
    def tribonacci(self, N: int) -> int:
        if N <= 2:
            return 0 if N == 0 else 1 

        dp = [0, 1, 1]
        

        for i in range(3, N+1):

            cur = dp[2] + dp[1] + dp[0]
            dp[2], dp[1], dp[0] = cur, dp[2], dp[1]
        
        return cur
