class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        def dfs(row, col):

            if not 0 <= row < R or not 0 <= col < C or grid[row][col] == 0:
                return 1

            if grid[row][col] == -1:
                return 0

            grid[row][col] = -1

            ans = 0
            for (
                dr,
                dc,
            ) in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nr, nc = row + dr, col + dc
                ans += dfs(nr, nc)

            return ans

        for row in range(R):
            for col in range(C):
                if grid[row][col] == 1:
                    return dfs(row, col)

        # return 