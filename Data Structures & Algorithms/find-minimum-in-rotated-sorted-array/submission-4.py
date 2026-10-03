class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left, right = 0, len(nums)-1

        res = float("inf")
        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break

            mid = (left + right) // 2

            res = min(res, nums[mid])
            if nums[left] > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return res




"""
[4, 5, 1, 2, 3]

"""