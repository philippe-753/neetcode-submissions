class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        cache = [[-1] * 2 for _ in range(N)]

        def dfs(i, buying):

            if i >= N:
                return 0
            
            if cache[i][buying] != -1:
                return cache[i][buying]
            
            if buying:
                cache[i][buying] = max(dfs(i+1, False) - prices[i], dfs(i+1, True))
            else:
                cache[i][buying] = max(dfs(i+2, True) + prices[i], dfs(i+1, False))
            
            return cache[i][buying]

        return dfs(0, True)