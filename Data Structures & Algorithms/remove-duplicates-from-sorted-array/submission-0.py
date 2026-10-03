class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        i = 0
        while i < N: 
            j = i + 1
            while j < N and nums[i] == nums[j]:
                j += 1
            nums[res] = nums[i]
            res += 1
            i = j 
        
        return res

            



        
        
