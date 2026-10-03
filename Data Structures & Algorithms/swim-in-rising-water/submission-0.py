import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        min_heap = []
        min_heap.append([grid[0][0], [0, 0]]) # cur_val, row, col, 
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()
        while min_heap:
            val, (row, col) = heapq.heappop(min_heap)
            visited.add((row, col))

            if (row == R-1) and (col == C-1):
                return val

            for dr, dc in dirs:
                nr, nc = row+dr, col+dc
                if 0<= nr < R and 0<=nc < C and (nr, nc) not in visited:
                    next_val = grid[nr][nc]
                    heapq.heappush(min_heap, [max(val, next_val), [nr, nc]])
        return -1