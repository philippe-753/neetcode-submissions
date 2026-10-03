class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        def dfs(row, col):
            if (not 0 <= row < R or not 0 <= col < C or grid[row][col] != 1):
                return 0
            
            grid[row][col] = 0
            area = 1
            for dr, dc in [[0, 1], [0, -1], [-1, 0], [1, 0]]:
                area += dfs(row + dr, col + dc)
                
            return area
        
        max_area = 0
        for row in range(R):
            for col in range(C):
                max_area = max(max_area, dfs(row, col))
        return max_area


        
