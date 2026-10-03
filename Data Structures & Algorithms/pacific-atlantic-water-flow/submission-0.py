class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])
        pas = [[False] * C for _ in range(R)]
        atl = [[False] * C for _ in range(R)]

        for col in range(C):
            pas[0][col] = True
            atl[-1][col] = True
        
        for row in range(R):
            pas[row][0] = True
            atl[row][-1] = True

        def dfs(row, col, water):
            water[row][col] = True
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = row+dr, col+dc
                if ((0 <= nr < R) and (0 <= nc < C) and
                 heights[nr][nc] >= heights[row][col] and
                not water[nr][nc]):
                    dfs(nr, nc, water)
        
        for row in range(R):
            for col in range(C):
                if pas[row][col]:
                    dfs(row, col, pas)
                    
        for row in range(R-1, -1, -1):
            for col in range(C-1, -1, -1):
                if atl[row][col]:
                    dfs(row, col, atl)
        
        print("pas:", pas)
        print("atl", atl)

        res = []
        for row in range(R):
            for col in range(C):
                if pas[row][col] and atl[row][col]:
                    res.append([row, col])
        
        return res

        

            
            

            


