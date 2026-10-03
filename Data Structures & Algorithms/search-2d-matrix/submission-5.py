class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        R, C = len(matrix), len(matrix[0])
        N = R*C

        left = 0
        right = N-1

        def idx_to_coordinate(idx:int) -> list:
            row = idx // C
            col = idx % C
            return [row, col]

        while left <= right:
            mid = (left + right)//2
            print("mid:", mid)
            row, col = idx_to_coordinate(mid)
            print("row, col:", row, col)

            if matrix[row][col] < target:
                left = mid + 1
            elif matrix[row][col] > target:
                right = mid - 1
            else:
                return True

        return False

            