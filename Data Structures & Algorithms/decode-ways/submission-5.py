class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        N = len(s)
        cache = [0] * N
        cache[-1] = 1


        def dfs(i):
            if i == N:
                return 1

            if s[i] == "0":
                return 0
            
            if cache[i]:
                return cache[i]

            cache[i] = dfs(i+1)
            if i + 1 < N and (s[i] == "1" or (s[i] == "2" and "0" <= s[i+1] <= "6")):
                cache[i] += dfs(i+2)
            return cache[i]
        
        return dfs(0)