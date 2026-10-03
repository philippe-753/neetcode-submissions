class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 2:
            return nums.index(target) if target in nums else -1
        return self.binary_search(0, len(nums)-1, nums, target)        


    def binary_search(self, left:int, right:int, nums: List[int], target:int) -> int:

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            if nums[left] ==  target:
                return left
            if nums[right] == target:
                return right
            # left is ordered.
            if nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else: # right hand side is ordered:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return idx if nums[mid] == target else -1



"""
[3,4,5,6,7,8,9,1,2]

"""

