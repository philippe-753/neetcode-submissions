class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N, M = len(word1), len(word2)
        cache = {}

        def dfs(i, j):
            
            if j == M:
                return N - i
            
            if i == N:
                return M - j
            
            if (i, j) in cache:
                return cache[(i, j)]
            
            move = float("inf")
            if word1[i] == word2[j]:
                move = dfs(i + 1, j + 1)
            
            insert = 1 + dfs(i, j + 1)
            delete = 1 + dfs(i + 1, j)
            replace = 1 + dfs(i + 1, j + 1)
            
            cache[(i, j)] = min(move, insert, delete, replace)
            return cache[(i, j)]
        
        return dfs(0, 0)
