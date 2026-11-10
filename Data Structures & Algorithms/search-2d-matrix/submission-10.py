class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C =  len(matrix), len(matrix[0])
        l, r = 0, R * C - 1

        while l <= r:
            mid = l + (r - l) // 2
            row, col =  mid // C, mid % C
            if row == R or row < 0:
                return False
            if matrix[row][col] < target:
                l = mid + 1
            elif matrix[row][col] > target:
                r = mid - 1
            else:
                return True
        
        return False
