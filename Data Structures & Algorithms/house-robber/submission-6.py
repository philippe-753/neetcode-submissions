class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 2: return max(nums)
        cache = [False] * (N)
        cache[0], cache[1] = nums[0], max(nums[0], nums[1])

        def dfs(i):
            if i == 0: return nums[0]
            if i == 1: return max(nums[0], nums[1])
            if cache[i]: return cache[i]
            cache[i] = max(dfs(i-1), dfs(i-2) + nums[i])
            return cache[i]
        
        dfs(N-1)

        return cache[-1]