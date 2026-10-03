class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left, right = 0, len(nums)-1

        res = float("inf")
        while left <= right:
            mid = (left + right) // 2
            
            res = min(res, nums[mid])
            if nums[left] > nums[mid]:
                right = mid - 1

            elif nums[right] < nums[mid]:
                left = mid + 1
            else:
                res = min(res, nums[left])
                break
        return res




"""
[4, 5, 1, 2, 3]

"""