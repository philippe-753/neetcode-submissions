class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        l, r = 0, N-1

        while l < r:
            for i in range(r-l):
                top, bot = l, r
                top_left = matrix[top][l + i]

                matrix[top][l + i] = matrix[bot-i][l]
                matrix[bot-i][l] = matrix[bot][r-i]
                matrix[bot][r-i] = matrix[top+i][r]
                matrix[top+i][r] = top_left

            l += 1
            r -= 1