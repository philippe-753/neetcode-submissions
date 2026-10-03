class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 2:
            return max(nums)
        
        # rom 0 - N-2
        dp = [0] * (N)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        
        for i in range(2, N-1):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
        dp[-1] = dp[-2]
        # rob from 1 - N-1
        dp2 = [0] * (N)
        dp[0], dp2[1], dp2[2] = 0, nums[1], max(nums[1], nums[2])
        for j in range(2, N):
            dp2[j] = max(nums[j] + dp2[j-2], dp2[j-1])
        
        return max(dp[-1], dp2[-1])

