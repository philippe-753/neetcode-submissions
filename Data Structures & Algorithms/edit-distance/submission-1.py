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
            
            if word1[i] == word2[j]:
                cache[(i, j)] = dfs(i + 1, j + 1)
            
            else:
                insert = 1 + dfs(i, j + 1)
                delete = 1 + dfs(i + 1, j)
                replace = 1 + dfs(i + 1, j + 1)
                cache[(i, j)] = min(insert, delete, replace)

            return cache[(i, j)]
        
        return dfs(0, 0)
