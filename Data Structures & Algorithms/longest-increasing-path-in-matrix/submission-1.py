class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        R = len(matrix)
        C = len(matrix[0])
        cache = [[None]*C for _ in range(R)]

        def dfs(row, col, prev):

            if row < 0 or row >= R or col < 0 or col >= C or prev >= matrix[row][col]:
                return 0
            
            if cache[row][col] is not None:
                return cache[row][col]
                
            res = 0
            for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                nr, nc = row + dr, col + dc
                res = max(res, 1 + dfs(nr, nc, matrix[row][col]))

            cache[row][col] = res
            
            return res

            
        res = 0
        for row in range(R):
            for col in range(C):
                res = max(res, dfs(row, col, -1))

        return res
        


            
                
                
            
