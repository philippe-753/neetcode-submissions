class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 2:
            return max(nums)

        dp = [0] * (N-1)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, N-1):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        dp2 = [0] * (N)
        dp2[1] = nums[1]
        dp2[2] = max(nums[1], nums[2])

        for i in range(3, N):
            dp2[i] = max(nums[i] + dp2[i-2], dp2[i-1])

        # print("dp:", dp)
        # print("dp2:", dp2)
        return max(dp[-1], dp2[-1])