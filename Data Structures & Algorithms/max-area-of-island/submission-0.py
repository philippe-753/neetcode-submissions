class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        def dfs(row, col):

            if row < 0 or col < 0 or row >= R or col >= C:
                return 0
            
            if grid[row][col] != 1:
                return 0
            
            grid[row][col] = "V"
            area = 1
            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                area += dfs(dr + row, dc + col)
            return area
        
        res = 0
        for row in range(R):
            for col in range(C):
                if grid[row][col] == 1:
                    res = max(res, dfs(row, col))
                    print("res:", res)
        return res

        
