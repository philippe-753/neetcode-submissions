class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        fruits = set()
        queue = deque([])

        for row in range(R):
            for col in range(C):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fruits.add((row, col))

        time = 0
        while queue and fruits:
            length = len(queue)
            for _ in range(length):
                row, col = queue.popleft()
                for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                    nr, nc = row+dr, col+dc
                    if (nr, nc) in fruits:
                        fruits.remove((nr, nc))
                        queue.append((nr, nc))
            time += 1
        
        return time if not fruits else -1

            