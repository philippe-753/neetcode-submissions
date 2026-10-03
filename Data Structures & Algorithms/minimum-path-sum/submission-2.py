import heapq
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        cache = [[float("inf")] * C for _ in range(R)]
        cache[R-1][C-1] = grid[R-1][C-1]

        def dfs(row, col):

            if not 0 <= row < R or not 0 <= col < C:
                return float("inf")
            
            if cache[row][col] != float("inf"):
                return cache[row][col]
            
            for dr, dc in [[1, 0], [0, 1]]:
                nr, nc = row + dr, col + dc
                cache[row][col] = min(cache[row][col], dfs(nr, nc) + grid[row][col])
            
            return cache[row][col]
        

        return dfs(0, 0)
            
