class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        N = len(nums)
        dp = [0] * (target + 1)
        dp[-1] = 1

        for i in range(target, -1, -1):
            for num in nums:
                if i - num >= 0:
                    dp[i - num] += dp[i]
        
        return dp[0]
            




