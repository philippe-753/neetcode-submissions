class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 1 and len(matrix[0]) == 1:
            return matrix[0]
        
        R, C = len(matrix), len(matrix[0])
        left, right = 0, C-1
        top, bot = 0, R-1 
        res = []
        
        while left <= right:
            for i in range(right-left+1):
                res.append(matrix[top][left + i])
            top += 1
            for i in range(bot-top+1):
                res.append(matrix[top+i][right])
            right -= 1
            if not (left <= right) or not (top <= bot):
                break
            # print("res0", res)
            for i in range(right-left+1):
                res.append(matrix[bot][right-i])
            bot -= 1
            if not (left <= right) or not (top <= bot):
                break
            for i in range(bot-top+1):
                res.append(matrix[bot-i][left])
            left += 1

        return res
            





