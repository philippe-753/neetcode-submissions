class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        cache = [[-1] * (amount + 1) for _ in range(N + 1)]

        
        def dfs(i, cur):

            if cur == 0:
                return 1

            if i == N or cur < 0:
                return 0
            
            if cache[i][cur] != -1:
                return cache[i][cur]
            
            cache[i][cur] = 0
            if cur > 0:
                cache[i][cur] = dfs(i + 1, cur) + dfs(i, cur - coins[i])
            
            return cache[i][cur]
        
        return dfs(0, amount)