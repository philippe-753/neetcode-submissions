class Solution:
    def trap(self, height: List[int]) -> int:
        # Two pointer solution, time O(n) space O(1)
        N = len(height)
        left = 0
        right = N-1

        max_left, max_right = 0, 0
        res = 0

        while left < right:
            max_left = max(max_left, height[left])
            max_right = max(max_right, height[right])
            if max_left <= max_right:
                res += max(max_left - height[left], 0)
                left += 1
            else:
                res += max(max_right - height[right], 0)
                right -= 1
        return res










        # prefix, suffix solution: Time: O(n)
        # N = len(height)
        
        # max_left = [0] * N
        # max_right = [0] * N

        # l_max = 0
        # for i, l_h in enumerate(height):
        #     max_left[i] = l_max
        #     l_max = max(l_max, l_h)
        
        # r_max = 0
        # for i in range(N-1, -1, -1):
        #     max_right[i] = r_max
        #     r_max = max(r_max, height[i])
        
        # res = 0
        # for i in range(N):
        #     res += max(min(max_left[i], max_right[i])-height[i], 0)
        
        # return res



            