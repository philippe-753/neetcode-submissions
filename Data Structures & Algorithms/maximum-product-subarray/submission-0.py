class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        res = -float("inf")
        for i in range(N):
            cur = nums[i]
            res = max(res, cur)
           
            for j in range(i+1, N):
                cur *= nums[j]
                res = max(res, cur)
        return res