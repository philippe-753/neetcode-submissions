import heapq
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        min_heap = [[grid[0][0], 0, 0]] # total count, row, col.
        heapq.heapify(min_heap)
        visited = set()


        while min_heap:
            total, row, col = heapq.heappop(min_heap)

            if row == R-1 and col == C-1:
                return total
            
            if (row, col) in visited:
                continue
            
            visited.add((row, col))

            if row + 1 != R:
                heapq.heappush(min_heap, [total + grid[row+1][col], row+1, col])
            if col + 1 != C:
                heapq.heappush(min_heap, [total + grid[row][col+1], row, col+1])
        
        return -1
            
