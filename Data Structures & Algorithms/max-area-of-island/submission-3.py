class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        def dfs(row, col):

            grid[row][col] = -1
            ans = 1
            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nr, nc = row + dr, col + dc
                if not 0 <= nr < R or not 0 <= nc < C or grid[nr][nc] != 1:
                    continue

                ans += dfs(nr, nc)

            return ans

        res = 0
        for row in range(R):
            for col in range(C):
                if grid[row][col] == 1:
                    res = max(res, dfs(row, col))

        return res