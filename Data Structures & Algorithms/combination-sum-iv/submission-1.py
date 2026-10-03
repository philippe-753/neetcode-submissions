class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        N = len(nums)
        memo = [False] * target

        def dfs(i, count):

            if count > target or i >= len(nums):
                return 0
            
            if count == target:
                return 1
            
            if memo[count]:
                return memo[count]

            take = 0
            for j in range(len(nums)):
                take += dfs(j, count + nums[j])
            
            memo[count] = take
            
            return take 
        
        return dfs(0, 0)



