class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)
        stack = [] # height, idx
        res = 0

        for idx, height in enumerate(heights):
            poped = False
            while stack and height < stack[-1][0]:
                poped = True
                stack_height, stack_idx = stack.pop()
                res = max(res, stack_height * (idx - stack_idx))

            if poped:
                stack.append([height, stack_idx])
            else:
                stack.append([height, idx])
        
        while stack:
            stack_height, stack_idx = stack.pop()
            res = max(res, stack_height * (N - stack_idx))

        return res