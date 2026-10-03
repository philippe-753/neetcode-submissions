class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        R, C = len(obstacleGrid), len(obstacleGrid[0])
        if R == 1 and C == 1 and obstacleGrid[0][0] == 0:
            return 1
        cache = [[-1] * C for _ in range(R)]


        def dfs(row, col):

            if not 0 <= row < R or not 0 <= col < C or obstacleGrid[row][col] == 1:
                return 0
            
            if row == R - 1 and col == C -1:
                return 1
            
            if cache[row][col] != -1:
                return cache[row][col]
            
            cache[row][col] = 0
            for dr, dc in [[0, 1], [1, 0]]:
                nr, nc = row + dr, col + dc
                cache[row][col] += max(dfs(nr, nc), 0)
            
            return cache[row][col]
        
        dfs(0, 0)
        print("cache:", cache)
        return cache[0][0] if cache[0][0] != -1 else 0


