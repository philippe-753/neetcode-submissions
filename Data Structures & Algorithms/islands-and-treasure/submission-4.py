class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R, C = len(grid), len(grid[0])
        inf_val = 2147483647

        # get all the tressures co-ordinates 
        queue = deque([])
        for row in range(R):
            for col in range(C):
                if grid[row][col] == 0:
                    queue.append((row, col, 0))
       
        while queue:
            row, col, level = queue.popleft()
            for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == inf_val:
                    grid[nr][nc] = level + 1
                    queue.append((nr, nc, level+1))

        

