class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        N = amount
        dp = [float("inf")] * (N + 1)
        for coin in coins:
            if coin < N:
                dp[coin] = 1
        dp[0] = 0
        
        for i in range(amount+1):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], 1 + dp[i - coin])

        return dp[-1] if dp[-1] != float("inf") else -1

                
               
        
