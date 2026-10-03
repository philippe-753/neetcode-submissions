class Solution:
    def uniquePaths(self, R: int, C: int) -> int:
        dp = [[0] * C for _ in range(R)]

        for row in range(R):
            dp[row][0] = 1
        
        for col in range(C):
            dp[0][col] = 1

        for row in range(1, R):
            for col in range(1, C):
                dp[row][col] = dp[row][col-1] + dp[row-1][col]
        
        return dp[R-1][C-1]