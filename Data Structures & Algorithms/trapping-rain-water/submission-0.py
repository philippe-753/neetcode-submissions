class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        
        max_left = [0] * N
        max_right = [0] * N

        l_max = 0
        for i, l_h in enumerate(height):
            max_left[i] = l_max
            l_max = max(l_max, l_h)
        
        r_max = 0
        for i in range(N-1, -1, -1):
            max_right[i] = r_max
            r_max = max(r_max, height[i])
        
        res = 0
        for i in range(N):
            res += max(min(max_left[i], max_right[i])-height[i], 0)
        
        return res



            