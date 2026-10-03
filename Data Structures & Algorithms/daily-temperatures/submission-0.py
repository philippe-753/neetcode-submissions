class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        stack = [] # temp, idx
        res = [0] * N

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_temp, stack_idx = stack.pop()
                res[stack_idx] = i - stack_idx

            stack.append([temp, i])

        return res