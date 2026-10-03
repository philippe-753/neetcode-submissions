class Solution:
    def tribonacci(self, N: int) -> int:
        if N <= 2:
            return 0 if N == 0 else 1 

        cache = [False for i in range(N+1)]
        cache[0], cache[1], cache[2] = 0, 1, 1

        def dfs(i):
            if i <= 0:
                return 0

            if cache[i]:
                return cache[i]

            cache[i] = dfs(i-1) + dfs(i-2) + dfs(i-3)
            return cache[i]
        

        dfs(N)
        return cache[-1]
            


