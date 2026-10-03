class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        res = set()
        print("nums:", nums)

        for left in range(N-2):
            middle = left + 1
            right = N -1
            while middle < right:
                cur_sum = nums[left] + nums[middle] + nums[right]
                if cur_sum < 0:
                    middle += 1
                elif cur_sum > 0:
                    right -=1
                else:
                    res.add((nums[left], nums[middle], nums[right]))
                    middle += 1

        print("res:", res)
        return list(res)