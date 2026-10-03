class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        def dfs(row, col):

            if (row < 0 or col < 0 or
                row >= R or col >= C):
                return None
            
            if grid[row][col] != "1":
                return None
            
            grid[row][col] = "V"

            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                dfs(row + dr, col + dc)
        
        res = 0
        for row in range(R):
            for col in range(C):
                if grid[row][col] == "1":
                    res +=1
                    dfs(row, col)
        
        return res