class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        res = []

        for left in range(N):
            if left > 0 and nums[left] == nums[left -1]:
                continue
            if nums[left] > 0:
                break
            
            middle = left + 1
            right = N -1
            while middle < right:
                cur_sum = nums[left] + nums[middle] + nums[right]
                if cur_sum < 0:
                    middle += 1
                elif cur_sum > 0:
                    right -=1
                else:
                    res.append([nums[left], nums[middle], nums[right]])
                    middle += 1
                    right -= 1
                    while middle < right and nums[middle] == nums[middle - 1]:
                        middle += 1

        return res