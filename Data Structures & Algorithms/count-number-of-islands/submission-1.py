class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        res = 0

        def dfs(row, col):

            if not 0 <= row < R or not 0 <= col < C or grid[row][col] == "V" or grid[row][col] == "0":
                return None 

            grid[row][col] = "V"

            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nr, nc = dr + row, dc + col
                dfs(nr, nc)

        for row in range(R):
            for col in range(C):
                if grid[row][col] == "1":
                    dfs(row, col)
                    res += 1           

        return res
