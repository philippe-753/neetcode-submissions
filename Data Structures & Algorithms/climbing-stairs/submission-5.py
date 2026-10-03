class Solution:
    def climbStairs(self, N: int) -> int:
        if N == 1:
            return 1

        dp = {}

        def dfs(i):

            if i <= 1:
                return 1
            
            if i in dp:
                return dp[i]
            
            dp[i] = dfs(i-1) + dfs(i-2)
            return dp[i]
        
        dfs(N)
        return dp[N]
