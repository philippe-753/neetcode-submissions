class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        self.nums = nums
        self.target = target
        return self.binary_search(l, r) 

    def binary_search(self, l, r):
        if l > r:
            return l 
        
        mid = (l + r) // 2
        if self.nums[mid] < self.target:
            return self.binary_search(mid + 1, r)

        elif self.nums[mid] > self.target:
            return self.binary_search(l, mid - 1)

        else:
            return mid


