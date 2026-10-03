class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not isinstance(grid, list):
            raise TypeError("grid input must be of time List")
        
        if not grid:
            raise ValueError("grid must be non empty list")
        
        if not isinstance(grid[0], list):
            raise TypeError(f"grid must be of type list[list] got {type(grid)}")

        R, C = len(grid), len(grid[0])
        queue = deque([])
        time = 0

        for row in range(R):
            for col in range(C):
                if grid[row][col] == 2:
                    queue.append((row, col, 0))

        while queue:
            row, col, time = queue.popleft()

            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1:
                    queue.append((nr, nc, time + 1))
                    grid[nr][nc] = 2
            
        
        return -1 if any(grid[row][col] == 1 for row in range(R) for col in range(C)) else time

     
    