class Solution:
    def maxArea(self, heights: List[int]) -> int:
        N = len(heights)
        l = 0
        r = N-1
        res = 0
        while l < r:
            l_h, r_h = heights[l], heights[r]
            res = max(res, min(l_h, r_h)*(r-l))
            if l_h < r_h:
                l += 1
            else:
                r -= 1
        
        return res
