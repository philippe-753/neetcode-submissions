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
            candidates = float("inf")
            # print("-------")
            # print("i", i)
            # print("dp:", dp)
            for coin in coins:
                cur = i
                cur -= coin
                if cur < 0 or dp[cur] == -1:
                    continue

                candidates = min(candidates, dp[cur])
                # print("coin:", coin)
                # print("cur:", cur)
                # print("candidates:", candidates)
            dp[i] = min(dp[i], 1 + candidates)
        
        # print("dp", dp)
        return dp[-1] if dp[-1] != float("inf") else -1

                
               
        
