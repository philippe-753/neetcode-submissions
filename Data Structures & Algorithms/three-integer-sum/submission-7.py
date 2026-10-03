class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        print("nums:", nums)
        res = []
        i = 0
        while i < N:
            while i > 0 and i + 1 < N and nums[i] == nums[i - 1]:
                i += 1

            l, r = i + 1, N - 1
            while l < r:
                cur = nums[i] + nums[l] + nums[r]
                if cur > 0:
                    r -= 1
                elif cur < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
            i += 1
        return res
