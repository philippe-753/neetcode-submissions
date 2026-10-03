class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        print("nums:", nums)
        res = []

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i -1]:
                continue
            if num > 0:
                break

            l, r = i + 1, N - 1
            while l < r:
                cur_sum = nums[i] + nums[l] + nums[r]
                if cur_sum > 0:
                    r -= 1
                elif cur_sum < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return res
            
