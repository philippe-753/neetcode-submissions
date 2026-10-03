class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R, C = len(grid), len(grid[0])
        inf_val = 2147483647

        def bfs(queue, visited):

            while queue:
                length = len(queue)
                for _ in range(length):
                    row, col, level = queue.popleft()
                    val = grid[row][col]
                    
                    grid[row][col] = min(val, level)
                    visited.add((row, col))

                    for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                        nr, nc = row + dr, col + dc
                        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != -1 and (nr, nc) not in visited:
                            queue.append([nr, nc, level+1])

        for row in range(R):
            for col in range(C):
                if grid[row][col] == 0:
                    visited = set()
                    queue = deque([[row, col, 0]])
                    bfs(queue, visited)
        # return grid

        

