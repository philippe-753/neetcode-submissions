class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])
        pas = [[False] * C for _ in range(R)]
        atl = [[False] * C for _ in range(R)]

        def dfs(row, col, water):
            water[row][col] = True
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = row+dr, col+dc
                if ((0 <= nr < R) and (0 <= nc < C) and
                 heights[nr][nc] >= heights[row][col] and
                not water[nr][nc]):
                    dfs(nr, nc, water)
        
        for col in range(C):
            dfs(0, col, pas)
            dfs(R-1, col, atl)
        
        for row in range(R):
            dfs(row, 0, pas)
            dfs(row, C-1, atl)

        res = []
        for row in range(R):
            for col in range(C):
                if pas[row][col] and atl[row][col]:
                    res.append([row, col])
        
        return res

        

            
            

            


